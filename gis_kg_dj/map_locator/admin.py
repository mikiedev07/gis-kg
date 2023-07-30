from django.contrib import admin

from .models import (
    Region,
    District,
    Canton,
    Contour
)

admin.site.register(Region)
admin.site.register(Contour)


@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ('title', 'district')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('title', 'region')
