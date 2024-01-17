from django.urls import path
from . import views

urlpatterns = [
    path('', views.rebrandly, name='rebrandly'),
]