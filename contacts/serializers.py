from rest_framework import serializers
from contacts import models


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefone
        fields = '__all__'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contato
        fields = '__all__'


class ContatoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContatoEndereco
        fields = '__all__'


class ContatoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContatoTelefone
        fields = '__all__'


class ContatoEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContatoEmail
        fields = '__all__'

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instituicao
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departamento
        fields = '__all__'


class InstituicaoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstituicaoEndereco
        fields = '__all__'


class DepartamentoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartamentoEndereco
        fields = '__all__'


class InstituicaoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstituicaoTelefone
        fields = '__all__'


class DepartamentoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartamentoTelefone
        fields = '__all__'


# class NotasSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Notas
#         fields = '__all__'
