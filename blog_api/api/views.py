from django.shortcuts import render
from .models import *

from django import forms
from django_editorjs_fields import EditorJsWidget


class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'
        widgets = {
            'body_editorjs': EditorJsWidget(config={'minHeight': 100}),
            'body_editorjs_text': EditorJsWidget(plugins=["@editorjs/image", "@editorjs/header"])
        }


def home(request):
    if request.method == 'POST':
        form = EditorForm(request.POST, request.FILES)
    else:
        form = EditorForm()
    editor = Editor.objects.all()
    context = {
        'editors': editor,
        'form': form,
    }
    return render(request, 'index.html', context)
