from django.db import models

# Create your models here.

from datetime import datetime
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birday  = models.DateField(verbose_name="生日",null=True,blank=True)
    gender = models.CharField(choices=(("male","男"),("woman","女")),max_length=20)
    address = models.CharField(max_length=100,default="")
    mphone  = models.CharField(max_length=11,null=True,blank=True)
    #这里头像具有上传功能，并且给他一个默认的头像值
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=200)


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table = "UserProfile"

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name="验证码")
    email = models.EmailField(max_length=50,verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型",choices=(('register',"注册"),('forget','找回密码')),max_length=20)
    send_time = models.DateField(default=datetime.now,verbose_name="发送时间")

    class Meta():
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name
        db_table = "EmailVerifyRecord"

    def __str__(self):
        return "邮箱验证码"


class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y%m",verbose_name="轮播图",max_length=50)
    url = models.URLField(max_length=200,verbose_name="访问地址")
    index = models.IntegerField(default=100,verbose_name="顺序")
    add_time = models.DateField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "轮播图"

