from django.db import models

from django_editorjs_fields import EditorJsTextField

class UploadImage(models.Model):
    content = models.TextField(default='Text Field', blank=True, null=True)
    image = models.ImageField(upload_to='image/upload/codex/%y/%m/%d/', blank=True, null=True)
    body_default = models.TextField(blank=True, null=True)
    body_editorjs_text = EditorJsTextField(blank=True, null=True)

    def __str__(self):
        return self.content