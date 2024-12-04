from django.db import models

from apps.cats.models import SpyCat


class Mission(models.Model):
    name = models.CharField(max_length=255)
    cat = models.OneToOneField(SpyCat, null=True, blank=True, on_delete=models.SET_NULL, related_name="mission")
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission: {self.name}"
