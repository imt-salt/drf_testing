# from rest_framework import viewsets
from rest_framework import views
from rest_framework.metadata import BaseMetadata
from rest_framework.response import Response

from policy.serializers import PolicySerializer


class MinimalMetadata(BaseMetadata):

    def determine_metadata(self, request, view):
        serializer = PolicySerializer()
        return {
            "type": view.get_view_name(),
            "fields": {k: str(v) for k, v in serializer.fields.items()}
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
