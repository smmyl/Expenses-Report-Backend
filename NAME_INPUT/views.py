from .serializers import NamesSerializer
from .models import Names
from django.shortcuts import render
from rest_framework import generics

class NamesList(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NamesSerializer

class NamesDetail(generics.RetrieveUpdateDeestroyAPIView):
    queryset = Names.objects.all().order_by('id')
    serializer_class = NamesSerializer