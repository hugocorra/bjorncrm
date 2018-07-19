from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
from rest_framework import generics

from contacts.forms import ContatoForm, TelefoneFormSet, EmailFormSet, EnderecoForm
from contacts.models import Contato, ContatoEndereco, ContatoTelefone, ContatoEmail
from contacts.serializers import ContatoSerializer


@login_required
def home(request):
    return render(request, 'contacts/index.html')


class ContatoApiList(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoList(ListView):
    model = Contato


class ContatoCreate(CreateView):
    template_name = 'contacts/contact_create_update.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contacts:contato-list')

    def get_context_data(self, **kwargs):
        context = super(ContatoCreate, self).get_context_data(**kwargs)
        context['form_endereco'] = EnderecoForm()
        context['formset_telefone'] = TelefoneFormSet()
        context['formset_email'] = EmailFormSet()
        return context


    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            super(ContatoCreate, self).post(request)
            endereco_form = EnderecoForm(request.POST)
            telefones_formset = TelefoneFormSet(request.POST)
            emails_formset = EmailFormSet(request.POST)

            if endereco_form.is_valid():
                endereco_obj = endereco_form.save()
                inst = ContatoEndereco(contato=self.object, endereco=endereco_obj)
                inst.save()
            else:
                print('E', endereco.errors)

            if telefones_formset.is_valid():
                for telefone_form in telefones_formset.forms:
                    telefone_obj = telefone_form.save()
                    inst = ContatoTelefone(contato=self.object, telefone=telefone_obj)
                    inst.save()
            else:
                print('E', telefones.errors)

            if emails_formset.is_valid():
                for email_form in emails_formset.forms:
                    email_obj = email_form.save()
                    inst = ContatoEmail(contato=self.object, email=email_obj)
                    inst.save()
            else:
                print('E', emails.errors)









class ContatoUpdate(CreateView):
    template_name = 'contacts/contact_create_update.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contacts:contato-list')