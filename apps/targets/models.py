from django.db import models

from apps.missions.models import Mission


class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Target: {self.name} ({'Complete' if self.is_complete else 'Incomplete'})"
