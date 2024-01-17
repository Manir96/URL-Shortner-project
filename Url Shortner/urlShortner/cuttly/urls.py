from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuttly, name='cuttly'),
]