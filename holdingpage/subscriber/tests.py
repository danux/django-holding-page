from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from holdingpage.subscriber.forms import SubscriberForm
from holdingpage.subscriber.models import Subscriber


class SubscriptionFormTestCase(TestCase):
    """
    Collection of tests to ensure the subscription form works correctly
    """
    fixtures = ['test_data.json']
    
    def setUp(self):
        self.data = {'full_name' : 'Test Name',
                     'email' : 'test@example.com'}
    
    def test_form_renders(self):
        """
        Tests that the form renders correctly
        """
        response = self.client.get(reverse('subscriber:subscriber_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['form'], SubscriberForm))
    
    def test_form_submits(self):
        """
        Tests that the form can be submitted with post, and the Fullname
        and email address are saved
        """
        response = self.client.post(reverse('subscriber:subscriber_form'), self.data)
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, reverse('subscriber:thank_you'))
        subscriber = Subscriber.objects.get(email='test@example.com',
                                            full_name='Test Name')

    def test_form_unique_email(self):
        """
        Tests that the form requires a unique email address
        """
        self.client.post(reverse('subscriber:subscriber_form'), self.data)
        response = self.client.post(reverse('subscriber:subscriber_form'), self.data)
        self.assertFormError(
                response,
                "form", 
                'email',
                u'Subscriber with this Email already exists.')

    def test_form_valid_email(self):
        """
        Tests that the form does not save details if the details provided
        are incorrect, i.e. badly formatted email address
        """
        data = {'email' : 'test@example'}
        response = self.client.post(reverse('subscriber:subscriber_form'), data)
        self.assertTrue(response.status_code, 200)
        self.assertFormError(
                response,
                "form", 
                'email',
                u'Enter a valid e-mail address.')

    def test_form_required_fields(self):
        """
        Tests that the form raises errors if required fields are not provided
        """
        data = {}
        response = self.client.post(reverse('subscriber:subscriber_form'), data)
        self.assertTrue(response.status_code, 200)
        self.assertFormError(
                response,
                "form", 
                'email',
                u'This field is required.')
        self.assertFormError(
                response,
                "form", 
                'full_name',
                u'This field is required.')
    
    def test_send_email(self):
        """
        Tests that an email is sent to new users, and that the email includes
        their sharing URL
        """
        response = self.client.post(reverse('subscriber:subscriber_form'), self.data)
        self.assertEqual(len(mail.outbox), 1)
    
    def test_subscription_share_code(self):
        """
        Tests that every new user has a share code generated and saved
        """
        response = self.client.post(reverse('subscriber:subscriber_form'), self.data)
        subscriber = Subscriber.objects.get(email='test@example.com',
                                            full_name='Test Name')
        self.assertTrue(subscriber.share_code is not None)
        self.assertTrue(len(subscriber.share_code) is 10)
    
    def test_form_renders_with_share_code(self):
        """
        Tests that a form is correctly rendered with a share code when one
        is provided
        """
        pass
    
    def test_form_saves_share_code(self):
        """
        Tests that a form submitted with a share code correctly saves the
        reference to this share code
        """
        referrer = Subscriber.objects.get(pk=1)
        response = self.client.get(reverse('subscriber:subscriber_form_with_code',
                                           args=[referrer.share_code]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial['source_share_code'], referrer.share_code)
    
    
    def test_form_valid_share_code(self):
        """
        Tests that a share code entered is actually valid, raises an error if not
        """
        self.data['source_share_code'] = '1234567890'
        response = self.client.post(reverse('subscriber:subscriber_form'),
                                    self.data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
                response,
                "form", 
                'source_share_code',
                u'Invalid share code.')
    
    def test_remove_email_address(self):
        """
        Tests that a user can unsubscribe their email address
        """
        pass