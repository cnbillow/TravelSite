from django.contrib import admin

# Register your models here.

from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "detail"]

admin.site.register(Company, CompanyAdmin)