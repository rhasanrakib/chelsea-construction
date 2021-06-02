from django import forms
from . models import Contact
class ContactForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Contact
        fields = ('name','email','message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-100 mb-3 p-3 large', 'Placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'w-100 mb-3 p-3 large', 'Placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'w-100 p-3 large','style':'border: transparent;','Placeholder': 'Message'}),
            
        }
    
