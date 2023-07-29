from rest_framework import serializers
from map_locator.models import (
    Region,
    District,
    Canton,
    Contour
)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
