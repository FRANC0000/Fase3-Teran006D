from django.urls import path
from . import views

urlpatterns =[

path('',views.index,name='index'),

path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name="cliente-detail"),
path('clientes/',views.ClienteListView.as_view(),name='clientes'),

path('boletas/', views.boletas, name='boletas'),

path('producto/<uuid:pk>/', views.ProductoDetailView.as_view(), name="producto-detail"),
path('productos/', views.ProductoListView.as_view(), name="productos"),
]

urlpatterns+=[
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),

    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),

    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    

    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),

    path('producto/<uuid:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    
    path('producto/<uuid:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),
]