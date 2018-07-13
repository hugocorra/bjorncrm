from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
from rest_framework import generics

from contacts.forms import ContatoForm, TelefoneFormSet, EmailFormSet
from contacts.models import Contato
from contacts.serializers import ContatoSerializer


@login_required
def home(request):
    return render(request, 'contacts/index.html')


class ContatoList(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoCreate(CreateView):
    template_name = 'contacts/contact_create_update.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato-list')

    def get_context_data(self, **kwargs):
        context = super(ContatoCreate, self).get_context_data(**kwargs)
        context['formset_telefone'] = TelefoneFormSet()
        context['formset_email'] = EmailFormSet()
        return context


class ContatoUpdate(CreateView):
    template_name = 'contacts/contact_create_update.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato-list')