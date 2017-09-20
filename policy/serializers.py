from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField

from policy.models import Policy, Coverage


class CoverageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coverage
        fields = ('liability', 'coverage_type')


class PolicySerializer(serializers.ModelSerializer):

    coverages = CoverageSerializer(
        # queryset=Coverage.objects,
        many=True
    )

    class Meta:
        model = Policy
        fields = ('policy_number', 'coverages')
