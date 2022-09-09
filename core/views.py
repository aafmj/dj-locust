from django.http import HttpResponse, JsonResponse
import time
from .models import Item
from django.shortcuts import get_object_or_404


def fast(request):
    return JsonResponse({"res": "FAST"})


def slow(request):
    time.sleep(2)
    return JsonResponse({"res": "SLOW"})


def get_item(request, id):
    obj = get_object_or_404(Item, pk=id)
    return JsonResponse({
        'name': obj.name,
        'id': obj.id
    })

