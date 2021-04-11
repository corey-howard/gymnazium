from django.contrib import admin

from.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'contact_date')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
