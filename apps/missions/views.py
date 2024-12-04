from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Mission
from .serializers import MissionSerializer
from apps.cats.models import SpyCat


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all().prefetch_related('targets')
    serializer_class = MissionSerializer

    # Disable the default update action
    def update(self, request, *args, **kwargs):
        return Response(
            {"error": "Direct mission updates are not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.cat is not None:
            return Response(
                {"error": "Cannot delete a mission assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        """
        Assign a mission to a cat.
        """
        mission = self.get_object()
        if mission.cat is not None:
            return Response(
                {"error": "This mission is already assigned to a cat."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cat_id = request.data.get("cat_id")
        if not cat_id:
            return Response(
                {"error": "cat_id is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            cat = SpyCat.objects.get(id=cat_id)
        except SpyCat.DoesNotExist:
            return Response(
                {"error": "Cat not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        mission.cat = cat
        mission.save()
        return Response(
            {"message": f"Mission {mission.name} assigned to cat {cat.name}."},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def mark_completed(self, request, pk=None):
        """
        Mark a mission as completed and also mark all related targets as completed.
        """
        mission = self.get_object()
        if mission.is_complete:
            return Response(
                {"error": "Mission is already completed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Mark the mission as completed
        mission.is_complete = True
        mission.save()

        # Mark all related targets as completed
        mission.targets.update(is_complete=True)

        return Response(
            {"message": f"Mission {mission.name} and all its targets have been marked as completed."},
            status=status.HTTP_200_OK,
        )
