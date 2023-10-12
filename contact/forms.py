from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            # 'first_name', # ERRO DO CAMPO (ABAIXO DO CAMPO)
            None,   # NON_FIELD_ERROR, (ABAIXO DO FORMULÁRIO)
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            # 'last_name', # ERRO DO CAMPO (ABAIXO DO CAMPO)
            None,   # NON_FIELD_ERROR, (ABAIXO DO FORMULÁRIO)
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()
