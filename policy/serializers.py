from rest_framework_json_api import serializers


class Policy():

    def __init__(self, *args, **kwargs):
        for field in ('id', 'policy_number'):
            setattr(self, field, kwargs.get(field, None))


class PolicySerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    policy_number = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Policy(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance
