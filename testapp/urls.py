"""Test app project urls."""
# Django
from django.urls import path

# Project
from testapp.views import TestPaypalView
from testapp.views import paypal_ipn

urlpatterns = [
    path('test/paypal/', TestPaypalView.as_view(), name='test_paypal'),
    path('paypal-ipn/', paypal_ipn, name='paypal_ipn'),
]
