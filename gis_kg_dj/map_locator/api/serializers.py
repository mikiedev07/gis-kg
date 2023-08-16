from rest_framework import serializers
from django.contrib.gis.geos import Polygon
from map_locator.models import (
    Region,
    District,
    Canton,
    TestContour,
)


class TestContourSerializer(serializers.ModelSerializer):
    geometry = serializers.SerializerMethodField()

    class Meta:
        model = TestContour
        fields = '__all__'

    def get_geometry(self, obj):
        if isinstance(obj.geometry, Polygon):
            coordinates = list(obj.geometry.coords[0])
            geojson = {
                "type": "Polygon",
                "coordinates": [coordinates]
            }
            return geojson
        return None


class CantonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canton
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    cantons = CantonSerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = '__all__'
