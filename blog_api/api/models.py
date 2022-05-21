from django.db import models

from django_editorjs_fields import EditorJsTextField

class Editor(models.Model):
    content = EditorJsTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}'