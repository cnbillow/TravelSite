from django.shortcuts import render

# Create your views here.
from apps.viewpoint.models import TravelPackage, Viewpoint, Location
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def getAttractions(request):
    """热门景点"""
    if request.method == "GET":
        all_view = Viewpoint.objects.all()  # 取出景点
        all_location = Location.objects.all()  # 所有地理位置(省份)

        # 筛选方式(sel):
        location_id = request.GET.get("sel", '')
        # location_id = int(location_id)

        # 筛选出所要求地域的景点
        if location_id:
            all_view = all_view.filter(address_id=int(location_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_view, 3, request=request)

        all_view = p.page(page)

        return render(request, "attractions.html", {
            "all_view": all_view,
            "all_location": all_location,
            "location_id": location_id,
        })


def getTravelPackage(request):
    """旅游套餐"""
    if request.method == "GET":
        all_package = TravelPackage.objects.all() # 所有旅游套餐
        # all_img = all_package.image_set.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_package, 3, request=request)

        all_package = p.page(page)

        return render(request, "set-meal.html", {
            "all_package": all_package,
        })


def getDetail(request, view_id):
    """景点详情"""
    if request.method == "GET":
        # 获取指定id的景点
        view = Viewpoint.objects.get(id=int(view_id))

        view_pics = view.images.all() # 景点图片

        return render(request, "detail.html", {
            "view": view,
            "view_pics": view_pics,
        })
