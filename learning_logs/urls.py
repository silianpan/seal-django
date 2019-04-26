#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 11:14
# @Author  : liupan
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topics/$', views.new_topic, name='new_topic')
]
