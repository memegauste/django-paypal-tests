"""Test everything file."""
from django.test import TestCase

from django.urls import reverse

from testapp.models import PaypalResponse


class TestEverything(TestCase):
    """Payment tests."""

    def setUp(self):
        pass

    def test_paypal_response_str_representation(self):
        """Test paypal response model."""
        obj = PaypalResponse()
        test_result = f'Created at: {obj.created_dt}'
        self.assertEqual(obj.__str__(), test_result)

    def test_paypal_ipn(self):
        """Test paypal ipn representation."""
        url = reverse('paypal_ipn')
        response = self.client.post(url, {'data': 'test'})
        queryset = PaypalResponse.objects.all()
        self.assertEqual(queryset.count(), 1)
        obj = queryset.first()
        self.assertEqual(obj.response, {'data': ['test']})
        self.assertEqual(response.content.decode(), 'OKAY')
