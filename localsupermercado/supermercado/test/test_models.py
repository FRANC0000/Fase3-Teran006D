from django.test import TestCase
from supermercado.models import Cliente, Producto, TipoProducto

# Create your tests here.

class ClienteModelTest(TestCase):
    @classmethod

    def setUp(cls):
        Cliente.objects.create(rut="203920040", dv="K", nombres="Test", apellidoP="Terán", apellidoM="Test", fcelular=0, fcasa=0, fecha_nacimiento="2000-10-30", email="test@super.cl")
    
    def test_rut_nombre_cliente(self):
        rutclient=Cliente.objects.get(rut="203920040")
        self.assertEqual(rutclient.apellidoP, "Terán")

#test models que reemplazan los test a form
class ProductoModelTest(TestCase):
    @classmethod

    def setUp(cls):
        Producto.objects.create(id_producto="5ce3dbbb-071d-4884-a03e-360ea424fa82",nombreP="Monitor LG", precio=158990, stock=10)
    
    def test_id_producto_nombre(self):
        idprod=Producto.objects.get(id_producto="5ce3dbbb-071d-4884-a03e-360ea424fa82")
        self.assertEqual(idprod.nombreP, "Monitor LG")

class TipoProductoModelTest(TestCase):
    @classmethod

    def setUp(cls):
        TipoProducto.objects.create(id_tipo="fbdd20ed-d62e-40b0-8606-b2c2af0364f8",tipo="Test")
    
    def test_id_tipo_nombre(self):
        idtipo=TipoProducto.objects.get(id_tipo="fbdd20ed-d62e-40b0-8606-b2c2af0364f8")
        self.assertEqual(idtipo.tipo, "Test")