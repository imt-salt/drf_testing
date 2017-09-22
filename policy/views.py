from rest_framework import generics
from rest_framework_json_api.views import RelationshipView

from policy.serializers import PolicySerializer, CoverageSerializer
from policy.models import Policy, Coverage


class CoverageView(generics.ListCreateAPIView):

    serializer_class = CoverageSerializer
    resource_name = 'coverage'
    queryset = Coverage.objects.all()


class PolicyView(generics.ListCreateAPIView):

    serializer_class = PolicySerializer
    resource_name = 'policy'
    queryset = Policy.objects.all()
