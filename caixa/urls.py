from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('opcoes/', views.opcoes, name="opcoes"),
    path('opcoes/depostio', views.deposito, name="deposito"),
    path('opcoes/saque', views.saque, name="saque")
]
