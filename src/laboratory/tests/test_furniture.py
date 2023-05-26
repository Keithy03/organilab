from django.urls import reverse

from laboratory.models import Shelf, Furniture, ShelfObject, LaboratoryRoom, TranferObject, Provider
from laboratory.tests.utils import BaseLaboratorySetUpTest
import json

class FurnitureViewTest(BaseLaboratorySetUpTest):

    def test_get_furniture_list_filter_by_labroom(self):
        url = reverse("laboratory:furniture_list", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        data = {
            "labroom": 2
        }
        response = self.client.get(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mueble 5", json.loads(response.content)['content']['inner-fragments']['#furnitures'])

    def test_get_furniture_list_filter_by_lab(self):
        url = reverse("laboratory:furniture_list", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mueble 2", json.loads(response.content)['content']['inner-fragments']['#furnitures'])

    def test_update_furniture(self):
        furniture = Furniture.objects.first()
        url = reverse("laboratory:furniture_update", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "pk": furniture.pk})

        response_get = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Mueble 1")

        # Updating furniture
        data = {
            "name": "Mueble Aéreo",
            "type": 75,
            "labroom": 1,
            "dataconfig": "[[], []]",
            "color": "#73879C"
        }
        response_post = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        success_url = reverse("laboratory:rooms_create", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        self.assertRedirects(response_post, success_url)
        self.assertIn("Mueble Aéreo", list(Furniture.objects.values_list("name", flat=True)))

    def test_create_furniture(self):
        labroom = LaboratoryRoom.objects.first()
        data = {
            "name": "Mueble Esquinero",
            "type": 75,
        }
        url = reverse("laboratory:furniture_create", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "labroom": labroom.pk})
        response = self.client.post(url, data=data)
        furniture = Furniture.objects.last()
        success_url = reverse("laboratory:furniture_update", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "pk": furniture.pk})
        self.assertRedirects(response, success_url)
        self.assertIn("Mueble Esquinero", list(Furniture.objects.values_list("name", flat=True)))

    def test_delete_furniture(self):
        furniture = Furniture.objects.get(name="Mueble 3")
        url = reverse("laboratory:furniture_delete", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "pk": furniture.pk})
        response = self.client.post(url)
        success_url = reverse("laboratory:rooms_create", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, success_url)
        self.assertNotIn("Mueble 3", list(Furniture.objects.values_list("name", flat=True)))

    def test_furniture_report_detail(self):
        data = {
            "pk": 1,
            "format": "pdf"
        }
        url = reverse("laboratory:reports_furniture_detail", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_add_furniture_type_catalog(self):
        url = reverse("laboratory:add_furniture_type_catalog")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class ShelfViewTest(BaseLaboratorySetUpTest):

    def test_update_shelf(self):
        shelf = Shelf.objects.first()
        url = reverse("laboratory:shelf_edit", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "pk": shelf.pk,
                                                       "row": shelf.row(), "col": shelf.col()})

        #Checking by method get if initial data shelf exists
        response_get = self.client.get(url, data={'furniture': shelf.furniture.pk}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, "Primer Estante")

        # Updating shelf
        data = {
            "shelf--name": "Estante central",
            "shelf--type": 74,
            "shelf--furniture": 1,
            "shelf--color": "#73879C",
            "shelf--row": 1,
            "shelf--col": 0,
            "shelf--in_where_laboratory": self.lab.pk,
            "shelf--discard": False,
            "shelf--quantity": 3,
            "shelf--description": "Estante de muestras",
            "shelf--measurement_unit": 59
        }
        response_post = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response_post.status_code, 200)
        self.assertIn("Estante central", json.loads(response_post.content)['content']['inner-fragments']['#shelfmodalbody'])

    def test_create_shelf(self):
        data = {
            "shelf--name": "Muestras",
            "shelf--type": 72,
            "shelf--furniture": 1,
            "shelf--color": "#73879C",
            "shelf--col": 0,
            "shelf--row": 2,
            "shelf--discard": False,
            "shelf--quantity": 3,
            "shelf--description": "Estante de muestras",
            "shelf--measurement_unit": 59,
            "shelf--in_where_laboratory": self.lab.pk,
        }
        url = reverse("laboratory:shelf_create", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk})
        response = self.client.post(url, data=data, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertIn("Muestras", list(Shelf.objects.values_list("name", flat=True)))
        self.assertEqual(response.status_code, 200)

    def test_delete_shelf(self):
        shelf = Shelf.objects.get(name="Noveno Estante")
        url = reverse("laboratory:shelf_delete", kwargs={"org_pk": self.org.pk, "lab_pk": self.lab.pk, "pk": shelf.pk,
                                                         "row": shelf.row(), "col": shelf.col()})
        response = self.client.post(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("Noveno Estante", list(Shelf.objects.values_list("name", flat=True)))

    def test_add_shelf_type_catalog(self):
        url = reverse("laboratory:add_shelf_type_catalog")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
