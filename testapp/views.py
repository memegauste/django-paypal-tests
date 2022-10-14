"""Testapp views file."""
# Standard Library
import urllib

# Django
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

# Project
from testapp.models import PaypalResponse


class TestPaypalView(TemplateView):
    """Test Paypal cyclic view."""

    template_name = 'cyclic_test.html'


@csrf_exempt
def paypal_ipn(request):
    """Paypal instant notification view."""
    uncleaned_request_data = urllib.parse.parse_qs(
        request.POST.urlencode(),
        keep_blank_values=True,
    )
    PaypalResponse.objects.create(
        response=uncleaned_request_data,
    )
    return HttpResponse('OKAY')
