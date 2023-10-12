from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    # PRIMEIRO JEITO - CRIA OU SOBRESCREVE UM WIDGET(CAMPO DO FORM)
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Primeiro nome',
            }
        ),
        label='Primeiro nome',
        help_text='Digite seu primeiro nome aqui',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # SEGUNDOS JEITO ATUALIZAR E ALTERA UM WIDGET JÁ EXISTENTE
        """ self.fields['first_name'].widget.attrs.update(
            {
                'class': 'classe-a classe-b',
                'placeholder': 'Primeiro nome',
            }
        ) """

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        # TERCEIRO JEITO CRIA OU SOBRESCREVE UM WIDGET
        """ widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'classe a',
                    'placeholder': 'Escreva aqui',
                }
            )
        } """

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
