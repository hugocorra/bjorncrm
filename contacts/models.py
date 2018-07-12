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
    TIPO_CONTATO = (
        ('P', 'Pessoal'),
        ('C', 'Comercial'),
    )

    nome = models.CharField(max_length=100, verbose_name='Nome')
    ocupação = models.CharField(max_length=50, verbose_name='Ocupação')
    cargo = models.CharField()
    tipo = models.CharField(choices=TIPO_CONTATO, max_length=1, verbose_name='Tipo')


class ContatoEndereco(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    #tipo = Residencial, Comercial, Outro

    class Meta:
        ordering = ('nome',)


class Instituicao(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Instituição')

    class Meta:
        ordering = ('nome',)


class Departamento(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Departamento')

    class Meta:
        ordering = ('nome',)


class ContatoTelefone(models.Model):
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


class InstituicaoEndereco(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class DepartamentoEndereco(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Departamento, on_delete=models.CASCADE)


class Notas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTime(auto_now=False, auto_now_add=False)
    texto = models.TextField(verbose_name='Nota')


class InstituicaoTelefone(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)


class DepartamentoTelefone(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)

