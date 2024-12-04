from rest_framework import serializers

from .models import SpyCat
from .services import is_breed_valid


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = "__all__"

    def validate_breed(self, value):
        if not is_breed_valid(value):
            raise serializers.ValidationError(f"The breed '{value}' is not valid")
        return value

    def update(self, instance, validated_data):
        """
        Override the update method to allow only the 'salary' field to be updated.
        """
        # Only allow the salary field to be updated
        salary = validated_data.get('salary')
        if salary is not None:
            instance.salary = salary

        instance.save()
        return instance
