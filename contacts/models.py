from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
    TIPO_CONTATO = (
        ('P', 'Pessoal'),
        ('C', 'Comercial'),
    )

    nome = models.CharField(max_length=100, verbose_name='Nome')
    ocupacao = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ocupação')
    tipo = models.CharField(choices=TIPO_CONTATO, max_length=1, verbose_name='Tipo')
    instituicao = models.CharField(max_length=50, blank=True, null=True, verbose_name='Instituição')
    departamento = models.CharField(max_length=50, blank=True, null=True, verbose_name='Departamento')
    notas = models.TextField(blank=True, verbose_name='Notas')


class Endereco(models.Model):
    pais = models.CharField(max_length=50, blank=True, null=True, verbose_name='País')
    estado = models.CharField(max_length=30, blank=True, null=True, verbose_name='Estado')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    logradouro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número')
    complemento = models.CharField(max_length=10, blank=True, null=True, verbose_name='Complemento')
    cep = models.CharField(max_length=9, blank=True, null=True, verbose_name='CEP')


class Telefone(models.Model):
    numero = models.CharField(max_length=20, blank=True, verbose_name='Telefone')


class Email(models.Model):
    email = models.EmailField(blank=True, verbose_name="E-mail")


class ContatoEndereco(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    #tipo = Residencial, Comercial, Outro


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


class ContatoEmail(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)


# class Notas(models.Model):
#     usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
#     texto = models.TextField(verbose_name='Nota')
