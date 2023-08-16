from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .api.serializers import (
    RegionSerializer,
    DistrictSerializer,
    CantonSerializer,
    TestContourSerializer,
)
from .models import Region, District, Canton, TestContour


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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


class TestContourView(viewsets.ModelViewSet):
    queryset = TestContour.objects.all()
    serializer_class = TestContourSerializer
    http_method_names = ['get']
