from rest_framework import routers
from django.urls import path

from .views import (
    RegionViewSet,
    DistrictViewSet,
    CantonListView,
    RegionListAPIView,
    TestContourView
)

app_name = 'map_locator'

region_router = routers.DefaultRouter()
district_router = routers.DefaultRouter()
canton_router = routers.DefaultRouter()
contour_router = routers.DefaultRouter()
test_router = routers.DefaultRouter()

region_router.register(r'regions', RegionViewSet, basename='regions')
district_router.register(r'districts', DistrictViewSet, basename='districts')
canton_router.register(r'cantons', CantonListView, basename='cantons')
test_router.register(r'test', TestContourView, basename='test')

# urlpatterns = [
#     path('test/', TestContourView.as_view(), name='test')
# ]
