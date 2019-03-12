# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

# 定义类GetReq，说明：主要存储get请求的path
class GetReq(models.Model):
    get_req_name = models.CharField(max_length=200,verbose_name='Get请求名称',blank=False,unique=True)
    get_path = models.CharField(max_length=500,verbose_name='请求路径')
    class Meta:
        verbose_name_plural = "Get请求"
    def __str__(self):
        return self.get_req_name

# 定义类PostReq，说明：主要存储post接口地址和post的内容
class PostReq(models.Model):
    post_req_name = models.CharField(max_length=200,verbose_name='Post接口名称',blank=False,unique=True)
    post_interface_url = models.URLField(max_length=200,verbose_name='Post接口地址',blank=False)
    post_content = models.TextField(max_length=10000,verbose_name='Post内容',blank=False)
    class Meta:
        verbose_name_plural = "Post请求"
    def __str__(self):
        return self.post_req_name

# 定义类AreUrl，说明：对某个地区做全流程测试，包括：多栏目Get和各种Post接口
class AreaUrl(models.Model):
    region = models.CharField(max_length=50,verbose_name='区域',blank=False,unique=True)
    getreqs = models.ManyToManyField(GetReq,verbose_name='Get接口',blank=True)
    ip = models.TextField(max_length=10000, verbose_name='Get-IP地址', blank=True, null=True)
    get_threshold = models.IntegerField(verbose_name='Get异常响应时间阈值(ms)',blank=True,null=True)
    postreq = models.ForeignKey(PostReq,on_delete=models.CASCADE,verbose_name='Post接口',blank=True,null=True)
    post_threshold = models.IntegerField(verbose_name='Post异常响应时间阈值(ms)', blank=True,null=True)
    class Meta:
        verbose_name_plural = "区域接口拨测"
    def __str__(self):
        return self.region
