#coding:utf-8
from django import template

register = template.Library()

@register.filter()
def isdig(value):
    """�������� �� ������������ �����"""
    return  value.replace('.','').replace('-','').isdigit()
