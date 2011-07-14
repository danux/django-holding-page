from django.conf.urls.defaults import *

urlpatterns = patterns("django.views.generic.simple",
                       url(r'^thank-you/$','direct_to_template', { 'template' : "subscriber/thank_you.html"}, name="thank_you"),)

urlpatterns += patterns("holdingpage.subscriber.views",
                        url(r'^(?P<code>[0-9A-Z]{10})$','subscriber_form', name="subscriber_form_with_code"),
                        url(r'','subscriber_form', name="subscriber_form"),)