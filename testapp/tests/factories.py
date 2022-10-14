"""Payments factories file."""
# 3rd-party
import factory
from factory import DjangoModelFactory

# Project
from testapp.models import PaypalResponse


def sequence(number):
    """Return a sequence."""
    return {
       'txn_type': ['recurring_payment'],
       'mc_gross': ['0.07'],
    }


class PaypalResponseFactory(DjangoModelFactory):
    """Paypal response factory."""

    response = factory.Sequence(sequence)

    class Meta:  # noqa: D106
        model = PaypalResponse
