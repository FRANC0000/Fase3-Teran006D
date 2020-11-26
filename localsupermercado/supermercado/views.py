from django.shortcuts import render
from . models import Producto, Cliente, TipoProducto
from django.views import generic

#formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	num_productos = Producto.objects.all()

	return render(
      request,
        'index.html',
        context={'num_productos':num_productos},

		)
def boletas(request):
    return render(
        request,
        'boletas.html'
        )  

#Admin
class TipoProductoCreate(CreateView):
    model = TipoProducto
    fields = ['tipo']

class TipoProductoUpdate(UpdateView):
    model = TipoProducto
    fields = ['tipo']

class TipoProductoDelete(DeleteView):
    model = TipoProducto
    success_url=reverse_lazy('index')

class TipoProductoDetailView(generic.DetailView):
    model = TipoProducto

class TipoProductoListView(generic.ListView):
    model = TipoProducto
    paginate_by = 20


class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombreP', 'stock', 'precio', 'imagen', 'id_tipo']

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombreP', 'stock', 'precio', 'imagen', 'id_tipo']
    template_name = 'supermercado/producto_update_form.html'

class ProductoDelete(DeleteView):
    model = Producto
    success_url=reverse_lazy('index')

class ProductoDetailView(generic.DetailView):
    model = Producto

class ProductoListView(generic.ListView):
    model = Producto
    paginate_by = 20


#Usuario
class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nombres','apellidoP', 'apellidoM', 'fcelular', 'fcasa','email']
    template_name_suffix = '_update_form'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('index')

class ClienteDetailView(generic.DetailView):
    model = Cliente


class ClienteListView(generic.ListView):
    model = Cliente
    paginate_by = 20

