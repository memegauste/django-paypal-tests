"""Test everything file."""
# Django
from django.test import TestCase
from django.urls import reverse

# Project
from testapp.models import PaypalResponse
from testapp.tests.factories import PaypalResponseFactory


class TestEverything(TestCase):
    """Payment tests."""

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

    def test_paypal_page(self):
        """Render the subscription page with Django templates and static files."""
        response = self.client.get(reverse('test_paypal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cyclic_test.html')
        self.assertContains(response, '/static/css/bootstrap.min.css')

    def test_paypal_response_factory(self):
        """Save and reload factory data through Django's JSONField."""
        obj = PaypalResponseFactory()
        obj.refresh_from_db()
        self.assertEqual(obj.response, {
            'txn_type': ['recurring_payment'],
            'mc_gross': ['0.07'],
        })
        self.assertIsNotNone(obj.created_dt)

    def test_paypal_ipn_preserves_repeated_and_empty_values(self):
        """Keep repeated and empty IPN fields when storing form data."""
        response = self.client.post(
            reverse('paypal_ipn'),
            'item_name=first&item_name=second&custom=',
            content_type='application/x-www-form-urlencoded',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(PaypalResponse.objects.get().response, {
            'item_name': ['first', 'second'],
            'custom': [''],
        })
