from django.urls import path
from . import views

urlpatterns = [
    path('iniciar/', views.Iniciar.as_view(), name='iniciar'),
]