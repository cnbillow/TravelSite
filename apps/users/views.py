from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views.generic.base import View


# class GetIndex(generic.ListView):
#     """主页"""
#     def get_queryset(self, request):
#         return render(request, "index.html", {})
from apps.viewpoint.models import Viewpoint, TravelPackage, Location


def getIndex(request):
    """主页"""
    views = Viewpoint.objects.all()[:6]  # 取出6个景点
    packages = TravelPackage.objects.all()[:3] # 取出3个旅游套餐
    locations = Location.objects.all()[:4]  # 4个地理位置(省份)
    if request.method == "GET":
        return render(request, "index.html", {
            "all_view": views,
            "packages": packages,
            "locations": locations,
        })


def getFeedback(request):
    """用户反馈"""
    if request.method == "GET":
        return render(request, "feedback.html", {})