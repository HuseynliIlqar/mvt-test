from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email.'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number.'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message', 'rows': 4}),
        }
