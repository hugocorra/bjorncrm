from django.db import models


class Endereco(models.Model):
    pais = models.CharField()
    estado = models.CharField()
    cidade = models.CharField()
    logradouro = models.CharField()
    numero = models.CharField()
    complemento = models.CharField()
    cep = models.CharField()


class Telefone(models.Model):
    numero = models.CharField()


class Contato(models.Model):
    nome = models.CharField()
    cargo = models.CharField()
    #tipo = Pessoal, Comercial


class ContatoEndereco(models.Model)
    contato = models.ForeignKey(Contato)
    endereco = models.ForeignKey(Endereco)
    #tipo = Residencial, Comercial, Outro


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato)
    telefone = models.ForeignKey(Telefone)


class Instituicao(models.Model):
    nome = models.CharField()


class Departamento(models.Model):
    nome = models.CharField()


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
    timestamp = models.DateTime()
    texto = models.TextField()
