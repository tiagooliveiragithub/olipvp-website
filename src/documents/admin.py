from django.contrib import admin
from .models import Document
from django_summernote.admin import SummernoteModelAdmin
from django.utils.safestring import mark_safe


@admin.register(Document)
class DocumentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = 'id', 'name', 'active', 'classification',
    list_display_links = 'name',
    search_fields = 'id', 'slug', 'name', 'content',
    list_filter = 'active',
    list_editable = 'active',
    ordering = 'classification', '-name',
    readonly_fields = (
        'created_at', 'updated_at', 'created_by', 'updated_by',
        'link',
    )
    prepopulated_fields = {
        "slug": ('name',),
    }

    def link(self, obj):
        if not obj.pk:
            return '-'

        url_of_document = obj.get_absolute_url()
        safe_link = mark_safe(
            f'<a target="_blank" href="{url_of_document}">See document</a>'
        )

        return safe_link

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        obj.save()


    
