from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.gis.geos import Polygon
from rest_framework.test import APIClient, APITestCase
from .models import Region, District, Canton, TestContour
from .api.serializers import RegionSerializer, TestContourSerializer


class RegionTestCase(TestCase):
    def setUp(self):
        self.region = Region.objects.create(title='Region 1', geometry='POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')

    def test_region_str(self):
        self.assertEqual(str(self.region), 'Region 1')

    def test_region_serializer(self):
        serializer = RegionSerializer(instance=self.region)
        self.assertEqual(serializer.data['title'], 'Region 1')


class RegionViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.region = Region.objects.create(title='Region 1', geometry='POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))')
        self.district = District.objects.create(
            title='District 1',
            region=self.region,
            geometry='POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))'
        )
        self.canton = Canton.objects.create(
            title='Canton 1',
            district=self.district,
            geometry='POLYGON((0 0, 0 1, 1 1, 1 0, 0 0))'
        )

    def test_get_region_list(self):
        response = self.client.get(reverse('regions-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_region_details(self):
        response = self.client.get(reverse('regions-detail', args=[self.region.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['region']['title'], 'Region 1')
        self.assertEqual(len(response.data['districts']), 1)
        self.assertEqual(len(response.data['cantons']), 1)

    def test_get_nonexistent_region(self):
        response = self.client.get(reverse('regions-detail', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestContourSerializerTestCase(APITestCase):
    def test_serializer_with_polygon(self):
        polygon_coords = ((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))
        polygon = Polygon(polygon_coords)
        test_contour = TestContour.objects.create(geometry=polygon)

        serializer = TestContourSerializer(instance=test_contour)
        expected_geojson = {
            "type": "Polygon",
            "coordinates": [list(polygon_coords)]
        }
        self.assertEqual(serializer.data['geometry'], expected_geojson)

    def test_serializer_with_invalid_geometry(self):
        invalid_geometry = "Invalid geometry string"
        test_contour = TestContour.objects.create(geometry=invalid_geometry)

        serializer = TestContourSerializer(instance=test_contour)
        self.assertIsNone(serializer.data['geometry'])
