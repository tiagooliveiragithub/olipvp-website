from django.shortcuts import render
from django.conf import settings
from helpers.minecraft import server_info
from .models import Rank
from documents.models import Document, DocumentType


def home(request):

    return render(
        request=request,
        template_name="main/home.html",
        context= {
            'page_title': "",
        })

def minecraft_data(request):
    data = server_info()
    return render(
        request=request,
        template_name="main/partials/minecraft_data.html",
        context= {
            'data': data,
        })

def server_guide(request):
    guide = Document.objects \
        .filter(classification=DocumentType.GUIDE) \
        .filter(active=True).filter(slug='guide') \
        .first()

    return render(
        request=request,
        template_name="main/guide.html",
        context= {
            'guide': guide,
            'page_title': "Guide - ",
        })

def server_guide_replace(request, page):
    if(page == "ranks"):
        ranks = Rank.objects.filter(active=True).order_by('level')
        return render(
            request=request,
            template_name="main/partials/ranks.html",
            context= {
                'ranks': ranks,
            })
    else:
        guide = Document.objects \
            .filter(classification=DocumentType.GUIDE) \
            .filter(active=True).filter(slug='guide') \
            .first()
        return render(
            request=request,
            template_name="main/partials/guide_manual.html",
            context= { 'guide': guide,})

def custom_404_view(request, exception):
        return render(request, '404_template.html', status=404)

    