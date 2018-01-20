from django.contrib import admin

# Register your models here.
from rango.models import category, page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title','category', 'url')
	
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
	
	
admin.site.register(category, CategoryAdmin)
admin.site.register(page, PageAdmin)

