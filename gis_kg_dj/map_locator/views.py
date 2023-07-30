from rest_framework import viewsets
from rest_framework.response import Response

from .api.serializers import (
    RegionSerializer,
    DistrictSerializer,
    CantonSerializer,
)
from .models import Region, District, Canton


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        districts = District.objects.filter(region=instance)
        district_serializer = DistrictSerializer(districts, many=True)
        cantons = Canton.objects.filter(district__region=instance)
        canton_serializer = CantonSerializer(cantons, many=True)
        data = {
            "region": serializer.data,
            "districts": district_serializer.data,
            "cantons": canton_serializer.data
        }
        return Response(data)


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        cantons = Canton.objects.filter(district=instance)
        canton_serializer = CantonSerializer(cantons, many=True)
        data = {
            "district": serializer.data,
            "cantons": canton_serializer.data
        }
        return Response(data)


class CantonListView(viewsets.ModelViewSet):
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer
    http_method_names = ['get']
