from django.db import models

class BoundingBox(models.Model):
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    x2 = models.IntegerField()
    y2 = models.IntegerField()
    image = models.ImageField(upload_to='images/')