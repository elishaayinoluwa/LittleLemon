from django.test import TestCase
from Restaurant.models import Menu



class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu(Title= 'Calamari', Price= 200, Inventory= 2)
        self.assertEqual(str(item), "Calamari : 200")

    