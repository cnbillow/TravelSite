from django.db import models

# Create your models here.


class Company(models.Model):
    """
    企业信息:
    名称 地址 介绍
    """
    name = models.CharField(verbose_name="企业名称", max_length=30)
    address = models.CharField(verbose_name="企业地址", max_length=100)
    detail = models.TextField(verbose_name="企业简介", default="")
    image = models.ImageField(verbose_name="照片", default="", upload_to="images/%Y/%m")

    class Meta:
        verbose_name = "企业信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
