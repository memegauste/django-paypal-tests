"""TestApp admin file."""
# Django
from django.contrib import admin


class PaypalResponseAdmin(admin.ModelAdmin):
    """Paypal response admin."""

    list_display = [
        'id',
        'created_dt',
    ]
