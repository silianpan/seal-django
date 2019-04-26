#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 22:37
# @Author  : liupan
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
