from django.http import JsonResponse
from django.shortcuts import render

from .forms import UploadForm

def index(request):
    form = UploadForm()

    return render(request, 'index.html', {'form': form})

def upload(request):
    if request.FILES:
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    
    return JsonResponse({'success': True})