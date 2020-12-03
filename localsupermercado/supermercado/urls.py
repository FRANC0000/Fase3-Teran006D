from django.urls import path
from . import views

urlpatterns =[

path('',views.index ,name='index'),

#cliente
path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name="cliente-detail"),
path('clientes/',views.ClienteListView.as_view(),name='clientes'),

path('boletas/', views.boletas, name='boletas'),

#producto
path('producto/<uuid:pk>/', views.ProductoDetailView.as_view(), name="producto-detail"),
path('productos/', views.ProductoListView.as_view(), name="productos"),

#tipoproducto
path('tipoproducto/<uuid:pk>/', views.TipoProductoDetailView.as_view(), name="tipoproducto-detail"),
path('tipoproductos/', views.TipoProductoListView.as_view(), name="tipoproductos"),
]

urlpatterns+=[
    #cliente
    path('cliente/create/', views.ClienteCreate.as_view(), name='cliente_create'),

    path('cliente/<int:pk>/update/', views.ClienteUpdate.as_view(), name='cliente_update'),

    path('cliente/<int:pk>/delete/', views.ClienteDelete.as_view(), name='cliente_delete'),
    
    #producto
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),

    path('producto/<uuid:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    
    path('producto/<uuid:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),

    #tipo de producto
    path('tipoproducto/create/', views.TipoProductoCreate.as_view(), name='tipoproducto_create'),

    path('tipoproducto/<uuid:pk>/update/', views.TipoProductoUpdate.as_view(), name='tipoproducto_update'),
    
    path('tipoproducto/<uuid:pk>/delete/', views.TipoProductoDelete.as_view(), name='tipoproducto_delete'),
]