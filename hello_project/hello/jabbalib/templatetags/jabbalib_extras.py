import json

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.template import Library

register = Library()


def jsonify(object):
    """
    https://djangosnippets.org/snippets/201/
    """
    if isinstance(object, QuerySet):
        return serialize('json', object)
    return json.dumps(object)


register.filter('jsonify', jsonify)
