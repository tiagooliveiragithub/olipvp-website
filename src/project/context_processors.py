from django.conf import settings
from documents.models import Document, DocumentType

def global_settings(request):
    """
    Injects global settings variables into the context.
    """
    return {
        'APP_NAME': settings.APP_NAME,
        'STAFF_EMAIL': settings.EMAIL_HOST_USER,
        'documents': Document.objects.filter(classification=DocumentType.IMPORTANT).filter(active=True).order_by('name'),
    }