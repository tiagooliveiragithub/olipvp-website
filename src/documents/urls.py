from django.urls import path
from . import views as documents_views

app_name = 'documents'

urlpatterns = [
    path('<slug:slug>/', documents_views.document, name='view'),
]