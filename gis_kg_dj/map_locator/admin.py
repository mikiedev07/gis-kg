from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from leaflet.admin import LeafletGeoAdmin

from .models import (
    Region,
    District,
    Canton,
    Contour,
    TestContour,
)

admin.site.register(Region)
admin.site.register(Contour)


class TestContourAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_CENTER': (51.5, -0.2),
        'DEFAULT_ZOOM': 10,
        'TILES': [
            ('OpenStreetMap', 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                'attribution': '© OpenStreetMap contributors'
            }),
            ('Google Maps', 'http://mt0.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {}),
        ],
    }
    base_layer = 1  # Индекс активного слоя по умолчанию


gis_admin.site.register(TestContour, TestContourAdmin)


@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ('title', 'district')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'region')



