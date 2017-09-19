from rest_framework_json_api import serializers


class PolicySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    policy_number = serializers.CharField(max_length=10)
    new_field = serializers.CharField(max_length=100)
