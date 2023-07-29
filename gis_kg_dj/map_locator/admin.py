from django.contrib import admin

from .models import (
    Region,
    District,
    Canton,
    Contour
)

admin.site.register(Region)
admin.site.register(District)
admin.site.register(Canton)
admin.site.register(Contour)
