#！/user/bin/python 
# -*- coding:utf-8 -*-  # 编码格式
# @Time: 2019/6/3 21:06   # 文件生成时间
# @Author: 朱金灿   # 作者
# @File: urls.py   # 文件名

from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]