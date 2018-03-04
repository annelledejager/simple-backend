from rest_framework import serializers
from simple_backend.models.colors import Colors


class ColorsSerializer(serializers.Serializer):
    color = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Colors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.colors = validated_data.get('colors', instance.title)
        instance.save()
        return instance
