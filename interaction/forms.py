from django.forms import ModelForm
from interaction import models


class InteracaoForm(ModelForm):
    class Meta:
        model = models.Interacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
