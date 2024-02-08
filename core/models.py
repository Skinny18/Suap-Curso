from django.db import models

# Create your models here.


class Usuario(models.Model):
    name = models.CharField(verbose_name='nome', max_length=100)
    email = models.EmailField(verbose_name='email', null=False)
    password = models.CharField(verbose_name='Senha',max_length=100, null=False)
