# Generated by Django 2.0.7 on 2018-07-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20180716_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='numero',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefone'),
        ),
    ]
