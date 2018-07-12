from django.db import models


class Endereco(models.Model):
    pais = models.CharField(max_length=50, verbose_name='País')
    estado = models.CharField(max_length=30, verbose_name='Estado')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    logradouro = models.CharField(max_length=100, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=10, verbose_name='Complemento')
    cep = models.CharField(max_length=9, verbose_name='CEP')


class Telefone(models.Model):
    numero = models.CharField(max_length=20, verbose_name='Telefone')


class Contato(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    ocupação = models.CharField(max_length=50, verbose_name='Ocupação')
    #tipo = Pessoal, Comercial


class ContatoEndereco(models.Model)
    contato = models.ForeignKey(Contato)
    endereco = models.ForeignKey(Endereco)


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato)
    telefone = models.ForeignKey(Telefone)


class Instituicao(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Instituição')


class Departamento(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Departamento')


class InstituicaoEndereco(models.Model):
    instituicao = models.ForeignKey(Instituicao)
    endereco = models.ForeignKey(Endereco)


class DepartamentoEndereco(models.Model):
    departamento = models.ForeignKey(Departamento)
    endereco = models.ForeignKey(Departamento)


class InstituicaoTelefone(models.Model):
    instituicao = models.ForeignKey(Instituicao)
    telefone = models.ForeignKey(Telefone)


class DepartamentoTelefone(models.Model):
    departamento = models.ForeignKey(Departamento)
    telefone = models.ForeignKey(Telefone)


class Notas(models.Model):
    usuario = models.ForeignKey(User)
    timestamp = models.DateTime(auto_now=False, auto_now_add=False)
    texto = models.TextField(verbose_name='Nota')
