from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/remover/<int:pk>/', views.cliente_delete, name='cliente_delete'),

    path('servicos/', views.servico_list, name='servico_list'),
    path('servicos/novo/', views.servico_create, name='servico_create'),
    path('servicos/editar/<int:pk>/', views.servico_edit, name='servico_edit'),
    path('servicos/remover/<int:pk>/', views.servico_delete, name='servico_delete'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)