from django.utils.translation import gettext_noop, gettext_lazy

# Compatibility layer for old translation functions
ugettext_noop = gettext_noop
ugettext_lazy = gettext_lazy

# Monkey-patch Django's translation module to provide ugettext_lazy
import django.utils.translation
django.utils.translation.ugettext_lazy = gettext_lazy 