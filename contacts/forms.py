from django.forms import ModelForm, BaseFormSet, formset_factory
from contacts import models # import Contato, Email, Telefone, Endereco


class ContatoForm(ModelForm):
    class Meta:
        model = models.Contato
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EmailForm(ModelForm):
    class Meta:
        model = models.Email
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class TelefoneForm(ModelForm):
    class Meta:
        model = models.Telefone
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EnderecoForm(ModelForm):
    class Meta:
        model = models.Endereco
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


TelefoneFormSet = formset_factory(
    TelefoneForm, can_delete=True, min_num=3)


EmailFormSet = formset_factory(
    EmailForm, can_delete=True, min_num=2)