from django.contrib import admin

# Register your models here.
from rango.models import category, page
admin.site.register(category)
admin.site.register(page)