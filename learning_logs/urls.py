#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 11:14
# @Author  : liupan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.index, name='index')
]
