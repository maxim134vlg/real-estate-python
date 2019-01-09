from django.contrib import admin
from realtors.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email')
	list_display_links = ('name',)
	search_fields = ('name',)
	list_per_page = 10
# Register your models here.
admin.site.register(Realtor, RealtorAdmin)