from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from api.views import upload

urlpatterns = [
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('upload/', upload, name='upload'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
