from django.contrib.gis.db import models


class Region(models.Model):
    title = models.CharField(max_length=50)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class Canton(models.Model):
    title = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    geometry = models.PolygonField()

    def __str__(self):
        return self.title


class Contour(models.Model):
    canton = models.ForeignKey(Canton, on_delete=models.SET_NULL, null=True)
    geometry = models.PolygonField()



