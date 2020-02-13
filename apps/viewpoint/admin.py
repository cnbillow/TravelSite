from django.contrib import admin

# Register your models here.
from apps.viewpoint.models import Viewpoint, Location, TravelPackage, PackageImage, ViewImage


class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "intr"]


class PackageImageInline(admin.TabularInline):
    model = PackageImage
    extra = 5


class ViewImageInline(admin.TabularInline):
    model = ViewImage
    extra = 5


class TravelPackageAdmin(admin.ModelAdmin):
    inlines = [PackageImageInline, ]
    list_display = ["name", "location", "price", "numbers", "evaluation", "intr"]

    def show_chapter_title(self, obj):
        return obj.chapter.title


class ViewpointAdmin(admin.ModelAdmin):
    inlines = [ViewImageInline, ]
    list_display = ["name", "address", "numbers", "score", "intr"]


admin.site.register(Viewpoint, ViewpointAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(TravelPackage, TravelPackageAdmin)
# admin.site.register(Image, ImageAdmin)
