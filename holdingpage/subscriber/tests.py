from django.test import TestCase


class SubscriptionFormTestCase(TestCase):
    """
    Collection of tests to ensure the subscription form works correctly
    """
    def test_form_renders(self):
        """
        Tests that the form renders correctly
        """
        pass
    
    def test_form_submits(self):
        """
        Tests that the form can be submitted with post, and the Fullname
        and email address are saved
        """
        pass
    
    def test_form_errors(self):
        """
        Tests that the form does not save details if the details provided
        are incorrect, i.e. badly formatted email address
        """
        pass
    
    def test_send_email(self):
        """
        Tests that an email is sent to new users, and that the email includes
        their sharing URL
        """
        pass
    
    def test_subscription_share_code(self):
        """
        Tests that every new user has a share code generated and saved
        """
        pass
    
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
        pass
    
    def test_remove_email_address(self):
        """
        Tests that a user can unsubscribe their email address
        """
        pass