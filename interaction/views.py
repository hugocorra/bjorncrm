from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from contacts.models import Contato
from interaction.forms import InteracaoForm
from interaction.models import Interacao, InteracaoContatos


class InteracaoList(ListView):
    model = Interacao

    #def get_context_data(self, **kwargs)


class InteracaoCreate(CreateView):
    template_name = 'interaction/interaction_create_update.html'
    form_class = InteracaoForm
    success_url = reverse_lazy('interaction:interacao-list')

    def get_context_data(self, **kwargs):
        context = super(InteracaoCreate, self).get_context_data(**kwargs)
        return context
