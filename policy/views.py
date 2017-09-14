from rest_framework import viewsets
from rest_framework.response import Response

from policy.serializers import PolicySerializer


class PolicyViewSet(viewsets.ViewSet):

    resource_name = 'policy'
    serializer_class = PolicySerializer

    # def list(self, request):
    #     serializer = PolicySerializer(instance=policies.values(), many=True)
    #     return Response(serializer.data)
