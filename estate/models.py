from django.db import models

class Estate(models.Model):
    estate_title = models.CharField()
    image = models.URLField()
    segment_name = models.CharField()
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField()
    area = models.CharField()
    location = models.CharField()
    facilities = models.JSONField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.estate_title
