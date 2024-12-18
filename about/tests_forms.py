from django.test import TestCase
from .forms import CollaborateForm

# Create your tests here.
class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields """
        form = CollaborateForm({
            'name': 'names',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg='Form is not Valid')

    def test_name_is_required(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Form is not valid because of the name field is empty')


    def test_email_is_required(self):
        form = CollaborateForm({
            'name': 'names',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Form is not valid because of the email field is empty')

    def test_message_is_required(self):
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg='Form is not valid because of the message field is empty')