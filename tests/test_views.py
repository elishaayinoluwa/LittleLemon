from Restaurant.views import MenuItemsView
from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient



class  MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.item1 = Menu.objects.create(Title= 'Spaghetti', Price= 1000, Inventory= 5)
        self.item2 = Menu.objects.create(Title= 'Rice&Beans', Price= 500, Inventory= 50)
        self.item3 = Menu.objects.create(Title= 'Garri', Price= 100, Inventory= 100)

    
    def test_getall(self):
        response = self.client.get('/restaurant/items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many= True)
        self.assertEqual(serializer.data, response.data)
