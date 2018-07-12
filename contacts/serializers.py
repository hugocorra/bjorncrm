from rest_framework import serializers
from contacts import models


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'


class ContatoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoEndereco
        fields = '__all__'


class ContatoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoTelefone
        fields = '__all__'


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class InstituicaoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoEndereco
        fields = '__all__'


class DepartamentoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoEndereco
        fields = '__all__'


class InstituicaoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituicaoTelefone
        fields = '__all__'


class DepartamentoTelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoTelefone
        fields = '__all__'


class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'
