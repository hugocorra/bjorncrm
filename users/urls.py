from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from users import views

app_name = 'users'

urlpatterns = [
    # path(r'list/', views.UserList.as_view(), name='users-list'),
    # path(r'users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    # path(r'users/add/', views.UserCreate.as_view(), name='user-create'),
    # path(r'users/update/<int:pk>/', views.UserUpdate.as_view(), name='user-update'),
    # path('login', TemplateView.as_view(template_name='users/login_simple.html'))
    path(r'users/signup/', views.signup, name='signup'),
]
