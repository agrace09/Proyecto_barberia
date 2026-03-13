from django import forms
from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    """Formulario de contacto"""
    
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu teléfono (opcional)'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escribe tu mensaje aquí...'
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Teléfono',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }
