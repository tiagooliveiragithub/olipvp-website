# urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('minecraft-data/', views.minecraft_data, name='minecraft_data'),
    path('guide/<str:page>/', views.server_guide_replace, name='guide_replacement'),
    path('guide/', views.server_guide, name='guide'),
    # Other paths...
]