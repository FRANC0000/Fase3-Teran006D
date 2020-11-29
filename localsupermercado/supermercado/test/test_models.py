from django.test import TestCase
from . models import Cliente, Producto, TipoProducto

# Create your tests here.

class ClienteModelTest(TestCase):
    @classmethod

    def setUp(self):
        Cliente.objects.create(rut="203920040",apellidoP="Terán")
    
    def test_rut_nombre_cliente(self):
        rutclient=Cliente.objects.get(rut="203920040")
        self.assertEqual(rutclient.apellidoP, "Terán")

class ProductoModelTest(TestCase):
    @classmethod

    def setUp(self):
        Producto.objects.create(id_producto="5ce3dbbb-071d-4884-a03e-360ea424fa82",nombreP="Monitor LG")
    
    def test_id_producto_nombre(self):
        idprod=Producto.objects.get(id_producto="5ce3dbbb-071d-4884-a03e-360ea424fa82")
        self.assertEqual(idprod.nombreP, "Monitor LG")

class TipoProductoModelTest(TestCase):
    @classmethod

    def setUp(self):
        TipoProducto.objects.create(id_tipo="fbdd20ed-d62e-40b0-8606-b2c2af0364fc",tipo="Animales")
    
    def test_id_tipo_nombre(self):
        idtipo=TipoProducto.objects.get(id_tipo="5ce3dbbb-071d-4884-a03e-360ea424fa82")
        self.assertEqual(idtipo.tipo, "Monitor LG")