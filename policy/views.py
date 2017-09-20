from rest_framework import generics
from rest_framework_json_api.views import RelationshipView

from policy.serializers import PolicySerializer
from policy.models import Policy, Coverage


# class CoverageRelationshipView(RelationshipView):
#     queryset = Coverage.objects


class PolicyView(generics.ListCreateAPIView):
    serializer_class = PolicySerializer
    resource_name = 'policy'
    queryset = Policy.objects.all()
