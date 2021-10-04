from django import forms
from django.forms.widgets import Textarea

class EmailForm(forms.Form):
    receiver = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=Textarea())

