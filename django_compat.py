from collections import OrderedDict

# Compatibility layer for removed Django utilities
class SortedDict(OrderedDict):
    """
    A dictionary that keeps its keys in the order in which they're inserted.
    This is a compatibility class to replace Django's removed SortedDict.
    """
    def __new__(cls, *args, **kwargs):
        instance = super(SortedDict, cls).__new__(cls, *args, **kwargs)
        instance.keyOrder = []
        return instance

    def __init__(self, data=None):
        super(SortedDict, self).__init__()
        if data:
            self.update(data)

def python_2_unicode_compatible(klass):
    """
    A decorator that defines __unicode__ and __str__ methods under Python 2.
    Under Python 3 it does nothing.
    
    To support Python 2 and 3 with a single code base, define a __str__ method
    returning text and apply this decorator to the class.
    """
    return klass 