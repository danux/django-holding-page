import random
import string

from django.db import models, IntegrityError
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.template.loader import render_to_string


class Subscriber(models.Model):
    """
    A subscriber represents a visitor to the holding page who has left
    their details behind.
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    share_code = models.CharField(max_length=10, null=True)
    source_share_code = models.CharField(max_length=10, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return '%s <%s>' % (self.full_name, self.email)
    
    class Meta():
        permissions = (
            ("export_csv", "Can export CSV data"),)
    
    @staticmethod
    def share_code_generator(sender, **kwargs):
        """
        Generates a unique share code for a subscriber using a ask for
        forgiveness, not permission, system
        """
        instance = kwargs['instance']
        if kwargs['created'] is False:
            return
        generated_unique_code = False
        while generated_unique_code is False:
            try:
                instance.share_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
                instance.save()
            except IntegrityError:
                pass
            else:
                generated_unique_code = True

    @staticmethod
    def send_email(sender, **kwargs):
        """
        Sends a welcome email to the user informing them about the share
        code, and also information about un-subscribing
        """
        instance = kwargs['instance']
        if kwargs['created'] is False:
            return
        site = Site.objects.get(id=settings.SITE_ID)
        subject = render_to_string('email/welcome_subject.txt', {'subscriber':  instance,
                                                                 'site' : site })
        body = render_to_string('email/welcome_body.txt', {'subscriber':  instance,
                                                           'site' : site })
        send_mail(subject,
                  body,
                  settings.DEFAULT_FROM_EMAIL,
                  [instance.email])
        

post_save.connect(Subscriber.share_code_generator, sender=Subscriber)
post_save.connect(Subscriber.send_email, sender=Subscriber)