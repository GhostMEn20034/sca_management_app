from rest_framework import serializers
from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"
        read_only_fields = ("mission", "is_complete")

