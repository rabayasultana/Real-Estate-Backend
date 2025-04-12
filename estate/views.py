from rest_framework import viewsets
from .models import Estate
from .serializers import EstateSerializer

class EstateViewSet(viewsets.ModelViewSet):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer
