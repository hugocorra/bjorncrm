# Generated by Django 2.0.7 on 2018-07-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20180713_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamentoendereco',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='departamentoendereco',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='departamentotelefone',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='departamentotelefone',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='instituicaoendereco',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='instituicaoendereco',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='instituicaotelefone',
            name='instituicao',
        ),
        migrations.RemoveField(
            model_name='instituicaotelefone',
            name='telefone',
        ),
        migrations.AddField(
            model_name='contato',
            name='departamento',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='contato',
            name='instituicao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='notas',
            field=models.TextField(blank=True, verbose_name='Nota'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='ocupacao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ocupação'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='pais',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='País'),
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.DeleteModel(
            name='DepartamentoEndereco',
        ),
        migrations.DeleteModel(
            name='DepartamentoTelefone',
        ),
        migrations.DeleteModel(
            name='Instituicao',
        ),
        migrations.DeleteModel(
            name='InstituicaoEndereco',
        ),
        migrations.DeleteModel(
            name='InstituicaoTelefone',
        ),
    ]