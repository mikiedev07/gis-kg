from rest_framework import routers

from .views import RegionListView

app_router = routers.DefaultRouter()
app_router.register(r'regions', RegionListView)
