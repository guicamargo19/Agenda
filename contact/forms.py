from django.core.exceptions import ValidationError
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
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
        )
        """ widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'classe a',
                    'placeholder': 'Escreva aqui',
                }
            )
        } """

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
