from django.contrib import admin

# Register your models here.
from rango.models import category, page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category', 'url')
	
admin.site.register(category)
admin.site.register(page, PageAdmin)

