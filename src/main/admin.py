from django.contrib import admin

# Register your models here.
from .models import Customer, Rank

admin.site.register(Customer)

@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = 'level','name', 'money', 'active',
    ordering = 'level',
    list_editable = 'active',
    list_display_links = 'name',