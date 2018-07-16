"""bjorncrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('', views.home, name='home'),
    path(r'contato/api/', views.ContatoApiList.as_view(), name='contato-api-list'),
    path(r'contato/api/<int:pk>/', views.ContatoApiDetail.as_view(), name='contato-api-details'),

    path(r'contato/', views.ContatoList.as_view(), name='contato-list'),
    path(r'contato/add/', views.ContatoCreate.as_view(), name='contato-create'),
    path(r'contato/update/<int:pk>/', views.ContatoUpdate.as_view(), name='contato-update'),
]
