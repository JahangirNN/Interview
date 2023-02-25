from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from home.models import NewUser
#  Register your models here.

admin.site.register(NewUser)
# admin.site.register(NewUser, UserAdmin)