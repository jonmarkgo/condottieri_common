from django.utils import datastructures
from .django_compat import SortedDict

# Monkey patch Django's datastructures to include SortedDict
datastructures.SortedDict = SortedDict

default_app_config = 'condottieri_common.apps.CondottieriCommonConfig'
