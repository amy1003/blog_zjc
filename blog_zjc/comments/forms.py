#！/user/bin/python 
# -*- coding:utf-8 -*-  # 编码格式
# @Time: 2019/6/3 21:01   # 文件生成时间
# @Author: 朱金灿   # 作者
# @File: forms.py   # 文件名

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']