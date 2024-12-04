from rest_framework import status, viewsets
from .models import SpyCat
from .serializers import SpyCatSerializer

class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
