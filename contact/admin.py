from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = '-id',
    list_per_page = 10
    list_max_show_all = 50
    list_filter = 'last_name',
    list_editable = 'phone',
    list_display_links = 'id', 'first_name',
    search_fields = 'id', 'first_name', 'last_name',

# Remy Lacroix
# Gold Starr
# Marsha May
# Leah Gotti
# Gabbie Carter
# Hazel Moore
