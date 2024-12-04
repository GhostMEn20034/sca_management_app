from rest_framework import serializers

from .models import Mission
from apps.targets.models import Target
from apps.targets.serializers import TargetSerializer


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = "__all__"

    @staticmethod
    def validate_target_count(targets_data):
        """
        Validates that the number of targets is between 1 and 3.
        """
        if not (1 <= len(targets_data) <= 3):
            raise serializers.ValidationError(
                "A mission must have between 1 and 3 targets."
            )
        return targets_data

    def create(self, validated_data):
        targets_data = validated_data.pop("targets")
        # Validate the number of targets before creation
        validated_targets = self.validate_target_count(targets_data)
        mission = Mission.objects.create(**validated_data)
        targets = [
            Target(mission=mission, **target_data) for target_data in validated_targets
        ]
        Target.objects.bulk_create(targets)
        return mission