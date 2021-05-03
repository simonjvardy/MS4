from django.test import TestCase, Client
from products.models import Product
# Create your tests here.


class TestCartViews(TestCase):
    """
    Tests the home page renders the correct page
    """
    def test_shopping_cart_page(self):
        response = self.client.get('/cart', follow=True)
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'cart/cart.html')

    def test_add_item_to_shopping_cart(self):
        pass