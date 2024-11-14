from django.db import models

class BoundingBox(models.Model):
    x1 = models.IntegerField()
    y1 = models.IntegerField()
    x2 = models.IntegerField()
    y2 = models.IntegerField()
    image = models.ImageField(upload_to='images/')

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MaskedImage(models.Model):
    original_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    masked_image = models.ImageField(upload_to='masked_images/')
    applied_at = models.DateTimeField(auto_now_add=True)