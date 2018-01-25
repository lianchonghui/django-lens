from django.contrib import admin

from .models import Lens
# Register your models here.

class LensAdmin(admin.ModelAdmin):
    list_display = ['name','description','full','thumb','author']

admin.site.register(Lens,LensAdmin)