from rest_framework import generics
from .serializers import NamesSerializer
from .models import Names


class NamesList(generics.ListCreateAPIView):
   queryset = Names.objects.all().order_by('id')
   serializer_class = NamesSerializer


class NamesDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Names.objects.all().order_by('id')
   serializer_class = NamesSerializer