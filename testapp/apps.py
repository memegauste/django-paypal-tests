"""Apps file."""
# Django
from django.apps import AppConfig


class TestappConfig(AppConfig):
    """Testapp config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
