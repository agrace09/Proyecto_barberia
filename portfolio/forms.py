from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    """Formulario de contacto"""
    
    class Meta:
       model = MensajeContacto
       fields = ['email', 'instagram', 'whatsapp']