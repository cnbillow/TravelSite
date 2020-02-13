"""TripDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from apps.users.views import GetIndex
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from TripDemo.settings import MEDIA_ROOT
from apps.company.views import getAboutWe, getContact
from apps.users.views import getIndex, getFeedback
from apps.viewpoint.views import getAttractions, getTravelPackage, getDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', getIndex, name="index"),  # 主页
    path('attractions/', getAttractions, name="attractions"),  # 热门景点
    path('travelPackage/', getTravelPackage, name="travelPackage"),  # 旅游套餐
    path('about/', getAboutWe, name="about"),  # 关于我们
    # path('feedback/', getFeedback, name="feedback"), # 用户反馈
    path('contact/', getContact, name="contact"),  # 联系我们
    path('detail/<int:view_id>', getDetail, name="detail"),  # 景点详细信息(景点信息页)




    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),  # 上传的文件


]
