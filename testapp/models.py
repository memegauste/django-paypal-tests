"""Test-App models file."""
# Django
from django.db import models


class PaypalResponse(models.Model):
    """Paypal response class."""

    response = models.JSONField('Paypal response')
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Created at: {self.created_dt}'

    class Meta:
        verbose_name = 'PayPal response'
        verbose_name_plural = 'PayPal responses'
