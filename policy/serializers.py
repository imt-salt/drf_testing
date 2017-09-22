from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from policy.models import Policy, Coverage


class CoverageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coverage
        fields = ('liability', 'coverage_type')


class PolicySerializer(serializers.HyperlinkedModelSerializer):

    coverages = ResourceRelatedField(
        many=True,
        related_link_view_name='policy:policy-coverages-list',
        related_link_url_kwarg='policy_pk',
        self_link_view_name='policy:policy_relationships',
        read_only=True
    )

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')
