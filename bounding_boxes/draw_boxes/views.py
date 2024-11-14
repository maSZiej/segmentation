from django.shortcuts import render
from .models import BoundingBox
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def save_bounding_boxes(request):
    if request.method == 'POST':
        boxes = request.POST.get('boxes')  # Oczekuj przesyłania danych w formacie JSON
        image_id = request.POST.get('image_id')

        # Przechowaj dane bounding box w bazie danych
        for box in boxes:
            BoundingBox.objects.create(
                x1=box['x1'], y1=box['y1'], x2=box['x2'], y2=box['y2'], image_id=image_id
            )
        return JsonResponse({'status': 'success'})
