import datetime

from django.db import models


# Create your models here.


class Location(models.Model):
    """
    地理位置:
    名称 位置 介绍 照片
    """
    name = models.CharField(verbose_name="地理位置名称", max_length=30, default="")
    address = models.CharField(verbose_name="所在地", max_length=100, default="")
    intr = models.TextField(verbose_name="介绍", default="")
    image = models.ImageField(verbose_name="照片", default="", upload_to="images/%Y/%m")

    class Meta:
        verbose_name = "地理位置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Viewpoint(models.Model):
    """
    景点信息:
    名称 位置 旅游人数 评分 简介 详细介绍 旅客评价
    """
    name = models.CharField(verbose_name="景点名称", max_length=30)
    address = models.ForeignKey(Location, verbose_name="位置", on_delete=models.CASCADE, default=0)  # 所在位置(外键-地理位置)
    numbers = models.IntegerField(verbose_name="旅游人数", default=0)
    score = models.CharField(verbose_name="评分", max_length=20, default="0")  # 用str类型存储的
    intr = models.CharField(verbose_name="简介", max_length=200, default="")
    detail = models.TextField(verbose_name="详细介绍", default="")
    image = models.ImageField(verbose_name="照片", default="", upload_to="images/%Y/%m")

    class Meta:
        verbose_name = "景点信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class TravelPackage(models.Model):
    """
    旅游套餐:
    套餐名称 目的地 价格 人数 简介 评分 照片
    """
    name = models.CharField(verbose_name="套餐名称", max_length=50, default="")
    location = models.CharField(verbose_name="目的地", max_length=50, default="")
    price = models.CharField(verbose_name="价格", max_length=20, default="")
    numbers = models.IntegerField(verbose_name="套餐包含人数", default=1)
    evaluation = models.FloatField(verbose_name="评分", default=3.0)
    intr = models.CharField(verbose_name="简介", max_length=200, default="")
    image = models.ImageField(verbose_name="照片", default="", upload_to="images/%Y/%m")
    # pics = models.ForeignKey(Image, verbose_name="相关照片", on_delete=models.CASCADE, default=0)

    class Meta:
        verbose_name = "旅游套餐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 图片列表
    # def get_image_list(self):
    #     return TravelPackage


class PackageImage(models.Model):
    package_img_list = models.ForeignKey(TravelPackage, related_name='images', on_delete=models.CASCADE, default=1)
    # view_img_list = models.ForeignKey(Viewpoint, related_name='images', on_delete=models.CASCADE, default=1)
    image = models.ImageField(verbose_name="套餐照片", default="", upload_to="images/%Y/%m")
    intr = models.CharField(verbose_name="描述", max_length=100, default="", null=True, blank=True)
    # addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        verbose_name = "套餐照片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s%s%s" % (self.package_img_list, self.image, self.intr)


class ViewImage(models.Model):
    # package_img_list = models.ForeignKey(TravelPackage, related_name='images', on_delete=models.CASCADE, default=1)
    view_img_list = models.ForeignKey(Viewpoint, related_name='images', on_delete=models.CASCADE, default=1)
    image = models.ImageField(verbose_name="景点照片", default="", upload_to="images/%Y/%m")
    intr = models.CharField(verbose_name="描述", max_length=100, default="", null=True, blank=True)
    # addtime = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now(), null=True, blank=True)


    class Meta:
        verbose_name = "景点照片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s%s%s" % (self.view_img_list, self.image, self.intr)