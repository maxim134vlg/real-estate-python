from django.contrib import admin
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'realtor', 'price', 'list_date', 'is_published')
	list_display_links = ('id', 'title', 'realtor')
	list_filter = ('realtor',)
	list_editable = ('is_published',)
	search_fields = ('id', 'title', 'city', 'price', 'state')
	list_per_page = 20
# Register your models here.
admin.site.register(Listing, ListingAdmin)