from django.urls import path
from . import views

urlpatterns = [
    path('', views.tiniurl, name='tiniurl'),
]