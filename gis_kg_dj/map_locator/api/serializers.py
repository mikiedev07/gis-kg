from rest_framework import serializers
from map_locator.models import (
    Region,
    District,
    Canton,
)


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
