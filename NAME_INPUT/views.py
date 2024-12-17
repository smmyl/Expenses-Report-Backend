from rest_framework import generics
from .serializers import NameSerializer
from .models import Name


class NameList(generics.ListCreateAPIView):
   queryset = Name.objects.all().order_by('id')
   serializer_class = NameSerializer


class NameDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Name.objects.all().order_by('id')
   serializer_class = NameSerializer