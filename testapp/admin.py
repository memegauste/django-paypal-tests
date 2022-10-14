"""TestApp admin file."""
# Django
from django.contrib import admin

# Project
from testapp.models import PaypalResponse


@admin.register(PaypalResponse)
class PaypalResponseAdmin(admin.ModelAdmin):
    """Paypal response admin."""

    list_display = [
        'id',
        'created_dt',
    ]
