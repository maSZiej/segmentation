from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save-bounding-boxes/', views.save_bounding_boxes, name='save_bounding_boxes'),
]
