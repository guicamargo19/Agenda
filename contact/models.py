from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# show (boolean), picture (imagem)
# category (foreign key), owner (foreign key)


# CADA MODEL CRIADO, OU ALTERADO PRECISAMOS FAZER AS MIGRAÇÕES

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, blank=True,
                                 on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, blank=True,
                              on_delete=models.SET_NULL, null=True)

    # Função que alterar o nome do objeto mostrado no formulário
    # inserido na base de dados
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
