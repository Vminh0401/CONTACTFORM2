from django.contrib import admin
from .models import Infor


# Register your models here.
class InforAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'select']


admin.site.register(Infor, InforAdmin)
