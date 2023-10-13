from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            message = ValidationError(
                'Senhas digitadas diferentes!',
                code='invalid'
            )

            # Adiciona um erro de propósito no campo em non-field
            self.add_error('first_name', message)
            self.add_error('last_name', message)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name in '1234567890':
            self.add_error(
                'first_name',
                ValidationError(
                    'Digite apenas letras',
                    code='invalid'
                )
            )

        return first_name
