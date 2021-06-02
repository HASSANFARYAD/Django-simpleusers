from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'phone')
    list_display_link = ('id', 'name')
    list_editable = ('gender', 'email', 'info', 'phone')
    list_per_page = 10
    search_fields = ('name', 'gender','email', 'info', 'phone')
    list_filter = ('gender', 'info', 'date_added')

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)


