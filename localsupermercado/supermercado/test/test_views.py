from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


from . models import Cliente, Producto, TipoProducto

#aquí tomé de referencia el proyecto cinecachupin.

class ClienteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_clientes = 23

        for clienterut in range(num_clientes):
            Cliente.objects.create(
                rut=f'20392004 {clienterut}',
                dv=f'{clienterut}',
                nombres = f'N {clienterut}',
                apellidoP= f'A paterno {clienterut}',
                apellidoM=f'A materno {clienterut}',
                fcelular = f'{clienterut}',
                fcasa = f' {clienterut}',
                fecha_nacimiento=f'{clienterut}/12/2020',
                email=f'supermercado{clienterut}@django.com',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/supermercado/clientes/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supermercado/cliente_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['cliente_list']) == 20)

    def test_lists_all_clientes(self):
        response = self.client.get(reverse('clientes')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['cliente_list']) == 3)


class TipoProductoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_tipo = 23
        
        for tipo_id in range(num_tipo):
            TipoProducto.objects.create(
                id_tipo=f'{tipo_id}',
                tipo=f'{tipo_id}',
            )

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/supermercado/tipoproductos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tipoproductos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('tipoproductos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supermercado/tipoproducto_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('tipoproductos'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['tipoproducto_list']) == 20)

    def test_lists_all_genres(self):
        response = self.client.get(reverse('tipoproductos')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['tipoproducto_list']) == 3)


class ProductoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_productos = 23
        p =TipoProducto.objects.create(
            id_tipo='uuid',
            tipo='Prueba'
        )
        with open('supermercado/static/img/leche.png') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/png')


        for id_prod in range(num_productos):
            test_prod = Producto.objects.create(
                id_producto=f'uuid {id_prod}',
                nombreP=f'prueba {id_prod}',
                stock =f'2 id_prod',
                preci =f'2000 id_prod',
                imagen = document,
                id_tipo = p,
            )
            
            test_prod.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/supermercado/productos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'supermercado/producto_list.html')
        