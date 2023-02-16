from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "subject",
            "message",
        )
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter your name", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email", "class": "form-control"}),
            "subject": forms.TextInput(attrs={"placeholder": "Enter the subject", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Enter your message", "class": "form-control"}),
        }
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "subject": "Subject",
            "message": "Message",
        }
        label_attrs = {
            "class": "control-label"
        }
