from django import forms
from .models import CollaborateRequest

#create your form here
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')