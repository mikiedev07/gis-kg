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


# class ContourSerializer(serializers.ModelSerializer): region_id = serializers.PrimaryKeyRelatedField(
# queryset=Region.objects.all(), source='canton__district__region_id') district_id =
# serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), source='canton__district_id') canton_id =
# serializers.PrimaryKeyRelatedField(queryset=Canton.objects.all())
#
#     class Meta:
#         model = Contour
#         fields = ['id', 'region_id', 'district_id', 'canton_id', 'geometry']
