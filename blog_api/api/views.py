from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def upload(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
    else:
        print(request)
    print(request.FILES)

    return JsonResponse({'success': 200})
