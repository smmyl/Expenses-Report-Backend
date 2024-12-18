from rest_framework import viewsets
from .serializers import NameSerializer
from .models import Name

class NameViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializer