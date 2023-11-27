from django.http.response import JsonResponse
from rest_framework import status

from core.models import ChordImages
from core.serializers import ChordImagesSerializer
from rest_framework.decorators import api_view

from core.services import scrape_for_images


@api_view(['GET'])
def get_chord_images(request):
    chord_name = request.GET.get('chord_name').lower()
    chord_images = ChordImages.objects.filter(chord_name = chord_name).first()

    if chord_images is not None:
        # ChordImages exists in db: serialize and return
        serializer = ChordImagesSerializer(chord_images)
        return JsonResponse(serializer.data, safe = False, status = status.HTTP_200_OK)

    # ChordImages does not exist in db: scrape, create and save
    images = scrape_for_images(chord_name)
    if not images:
        return JsonResponse(None, safe = False, status = status.HTTP_404_NOT_FOUND)

    chord_images = ChordImages(chord_name = chord_name, images = images)
    chord_images.save()
    serializer = ChordImagesSerializer(chord_images)
    return JsonResponse(serializer.data, safe = False, status = status.HTTP_200_OK)
