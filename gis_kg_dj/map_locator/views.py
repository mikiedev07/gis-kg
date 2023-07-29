from django.shortcuts import render
from rest_framework import viewsets

from .api.serializers import RegionSerializer
from .models import Region, District, Canton


class RegionListView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictListView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = RegionSerializer


class CantonListView(viewsets.ModelViewSet):
    queryset = Canton.objects.all()
    serializer_class = RegionSerializer
