# from rest_framework import viewsets
from collections import defaultdict
import itertools

from rest_framework import views
from rest_framework.metadata import BaseMetadata
from rest_framework.response import Response

from policy.serializers import PolicySerializer


class MinimalMetadata(BaseMetadata):

    def determine_metadata(self, request, view):
        desired_fields = (
            'type', 'name', 'allow_blank', 'allow_null', 'label',
            'required', 'read_only', 'max_length'
        )
        serializer = PolicySerializer()
        fields = defaultdict(dict)
        for serializer_fields, desired in itertools.product(serializer.fields.items(), desired_fields):
            name, attrs = serializer_fields
            if hasattr(attrs, desired):
                fields[name][desired] = getattr(attrs, desired)
        return {
            "type": view.get_view_name(),
            "fields": fields
        }


class PolicyView(views.APIView):

    resource_name = 'policy'
    metadata_class = MinimalMetadata

    def post(self, request, format=None):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            data = {
                "error": True,
                "errors": serializer.errors,
            }
            return Response(data)

    def get(self, request, **kwargs):
        meta = self.metadata_class()
        data = meta.determine_metadata(request, self)
        return Response(data)
