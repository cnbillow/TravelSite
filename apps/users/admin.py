from django.contrib import admin

# Register your models here.
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "password", "age", "gender", "address", "selfintr"]

admin.site.register(User, UserAdmin)
