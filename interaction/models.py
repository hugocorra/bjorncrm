from django.db import models


class Interacao(models.Model):
    resumo = models.CharField(max_length=150, blank=True, null=True, verbose_name="Resumo")
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data = models.DateField(verbose_name='Data')
    horario = models.TimeField(blank=True, null=True, verbose_name='Horário')


class InteracaoContatos(models.Model):
    contato = models.ForeignKey('contacts.Contato', on_delete=models.CASCADE)
    interacao = models.ForeignKey(Interacao, on_delete=models.CASCADE)
