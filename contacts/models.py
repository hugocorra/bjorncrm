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

    class Meta:
        ordering = ('nome',)


class ContatoEndereco(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    #tipo = Residencial, Comercial, Outro


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


class Instituicao(models.Model):
    nome = models.CharField()

    class Meta:
        ordering = ('nome',)


class Departamento(models.Model):
    nome = models.CharField()

    class Meta:
        ordering = ('nome',)


class InstituicaoEndereco(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class DepartamentoEndereco(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Departamento, on_delete=models.CASCADE)


class InstituicaoTelefone(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


class DepartamentoTelefone(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


# class Notas(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTime()
#     texto = models.TextField()
