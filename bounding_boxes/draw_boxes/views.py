from django.shortcuts import render
from .models import BoundingBox
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.conf import settings
import json
import base64
from io import BytesIO
from PIL import Image as PILImage
import numpy as np

def index(request):
    return render(request, 'index.html')

def bounding_box(request):
    return render(request, 'main.html')


def segmentation(request):
    return render(request, 'segmentation.html')

def save_bounding_boxes(request):
    if request.method == 'POST':

        # Sprawdź dane przychodzące
        data = json.loads(request.body)
        boxes = data.get('boxes', None)
        image_id= data.get('image_id',)
        #boxes = request.POST.get('boxes')  # Oczekuj przesyłania danych w formacie JSON
        #image_id = request.POST.get('image_id')

        # Przechowaj dane bounding box w bazie danych
        for box in boxes:
            BoundingBox.objects.create(
                x1=box['x1'], y1=box['y1'], x2=box['x2'], y2=box['y2']
            )
        return JsonResponse({'status': 'success'})


'''
def upload_image(request):
    if request.method == 'POST' and request.FILES['imageFile']:
        image_file = request.FILES['imageFile']
        file_path = default_storage.save(f"images/{image_file.name}", image_file)
        image_url = settings.MEDIA_URL + file_path
        return JsonResponse({'image_url': image_url})
    return JsonResponse({'error': 'No file uploaded'}, status=400)
'''
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('imageFile'):
        image_file = request.FILES['imageFile']
        # Zapisz plik bezpośrednio w MEDIA_ROOT
        file_path = default_storage.save(image_file.name, image_file)
        image_url = settings.MEDIA_URL + file_path  # Ścieżka dostępu do pliku
        return JsonResponse({'image_url': image_url})
    return JsonResponse({'error': 'No file uploaded'}, status=400)

from django.shortcuts import render
from .models import Image
from .forms import ImageUploadForm

def draw_mask(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'draw_mask.html', {'image': image})


def save_mask(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        mask_image_data = data['mask_image']

        # Usuń początek DataURL
        image_data = mask_image_data.split(',')[1]
        image_data = base64.b64decode(image_data)

        # Zapisz obraz
        image = PILImage.open(BytesIO(image_data))
        image_path = 'path/to/save/mask_image.png'
        image.save(image_path)

        # Możesz teraz zapisać obraz w modelu lub zrobić inne operacje
        return JsonResponse({'message': 'Maska została zapisana'})