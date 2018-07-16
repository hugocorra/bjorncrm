from django.forms import ModelForm
from interaction import models

class InteracaoForm(ModelForm):
    class Meta:
        model = models.Interacao
        fields = '__all__'


