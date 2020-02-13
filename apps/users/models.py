from django.db import models

# Create your models here.

class User(models.Model):
    """
    用户信息:
    姓名 邮箱 密码 年龄 性别 地址 自我介绍
    """
    name = models.CharField(verbose_name="姓名", max_length=20)
    email = models.CharField(verbose_name="邮箱", max_length=50, default="")
    password = models.CharField(verbose_name="密码", max_length=100)
    age = models.IntegerField(verbose_name="年龄", default=18)
    gender = models.CharField(verbose_name="性别", max_length=6, choices=[("male", "男"), ("female", "女")], default="male")
    address = models.CharField(verbose_name="地址", max_length=200, default="")
    selfintr = models.TextField(verbose_name="自我介绍", default="")
    image = models.ImageField(verbose_name="照片", default="", upload_to="images/%Y/%m")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


