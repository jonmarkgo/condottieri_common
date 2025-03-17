from django.apps import AppConfig

class CondottieriCommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'condottieri_common'
    verbose_name = 'Condottieri Common'

    def ready(self):
        # Import and apply our compatibility layers
        from django.utils import datastructures, encoding
        from .django_compat import SortedDict, python_2_unicode_compatible
        datastructures.SortedDict = SortedDict
        encoding.python_2_unicode_compatible = python_2_unicode_compatible 