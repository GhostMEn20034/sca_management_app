from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Target
from .serializers import TargetSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response(
            {"error": "Direct mission updates are not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Prevent listing targets
    def list(self, request, *args, **kwargs):
        return Response(
            {"error": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Prevent updating targets
    def update(self, request, *args, **kwargs):
        return Response(
            {"error": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"error": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Prevent deleting targets
    def destroy(self, request, *args, **kwargs):
        return Response(
            {"error": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    # Mark target as completed
    @action(detail=True, methods=["post"])
    def mark_completed(self, request, pk=None):
        """
        Mark a target as completed and check if all related targets in the mission are completed.
        If all targets are completed, the mission will also be marked as completed.
        """
        target = self.get_object()
        if target.is_complete:
            return Response(
                {"error": "Target is already completed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        target.is_complete = True
        target.save()

        # Check if all targets of the related mission are completed
        mission = target.mission
        all_targets_completed = mission.targets.filter(is_complete=False).count() == 0

        # If all targets are completed, mark the mission as completed
        if all_targets_completed:
            mission.is_complete = True
            mission.save()

        return Response(
            {"message": f"Target {target.name} has been marked as completed."},
            status=status.HTTP_200_OK,
        )

    # Update the notes of a target
    @action(detail=True, methods=["post"])
    def update_notes(self, request, pk=None):
        """
        Update the notes of a target.
        Notes cannot be updated if the target or its mission is completed.
        """
        target = self.get_object()

        if target.is_complete:
            return Response(
                {"error": "Cannot update notes for a completed target."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mission = target.mission
        if mission.is_complete:
            return Response(
                {"error": "Cannot update notes for a target of a completed mission."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        notes = request.data.get("notes")
        if notes:
            target.notes = notes
            target.save()
            return Response(
                {"message": f"Notes for target {target.name} have been updated."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "Notes are required to update."},
            status=status.HTTP_400_BAD_REQUEST,
        )