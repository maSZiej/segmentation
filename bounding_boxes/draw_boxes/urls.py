from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segmentation', views.segmentation, name='segmentation'),
    path('bounding_box', views.bounding_box, name='bounding_box'),
    path('save_mask', views.save_mask, name='save_mask'),
    path('save-bounding-boxes/', views.save_bounding_boxes, name='save_bounding_boxes'),
     path('upload/', views.upload_image, name='upload_image'),
]


# Umożliw Django obsługę plików media podczas rozwoju
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
