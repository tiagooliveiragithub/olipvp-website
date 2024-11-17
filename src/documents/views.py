from django.shortcuts import render
from .models import Document

# Create your views here.

def document(request, slug):
    document = Document.objects.get(slug=slug)
    context = {
            'page_title': f' {document.name} - ',
            'document': document,
    }

    return render(request, 'documents/document.html', context)
