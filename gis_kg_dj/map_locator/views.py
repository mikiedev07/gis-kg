from django.shortcuts import render
from rest_framework import viewsets, generics, views, status
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


# class ContourFilter(django_filters.FilterSet):
#     region = django_filters.CharFilter(field_name='canton__district__region__title')
#     district = django_filters.CharFilter(field_name='canton__district__title')
#     canton = django_filters.CharFilter(field_name='canton__title')
#     region_id = django_filters.NumberFilter(field_name='canton__district__region__id')
#     district_id = django_filters.NumberFilter(field_name='canton__district__id')
#     canton_id = django_filters.NumberFilter(field_name='canton__id')
#
#     class Meta:
#         model = Contour
#         fields = []


# class ContourViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ContourSerializer
#     filterset_class =
#
#     def get_queryset(self):
#         cid = self.request.query_params.get('canton_id', None)
#         print(cid)
#         if cid is not None:
#             canton = Canton.objects.get(id=cid)
#             return Contour.objects.filter(canton=canton)
#         return status.HTTP_404_NOT_FOUND


# class ContourListAPIView(viewsets.ReadOnlyModelViewSet):
#     queryset = Contour.objects.all()
#     serializer_class = ContourSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     filterset_class = ContourFilter
