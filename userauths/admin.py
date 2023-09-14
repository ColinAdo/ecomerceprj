from django.contrib import admin
from .models import CustomUser

class UserAdamin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

admin.site.register(CustomUser, UserAdamin)
