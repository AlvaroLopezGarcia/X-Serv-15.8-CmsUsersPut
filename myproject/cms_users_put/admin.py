from django.contrib import admin
from django.contrib.auth.views import logout, login

# Register your models here.

from .models import Pages

admin.site.register(Pages)
