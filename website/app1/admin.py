from django.contrib import admin

# Register your models here.

from .models import Users,Blog

admin.site.register(Users)
admin.site.register(Blog)