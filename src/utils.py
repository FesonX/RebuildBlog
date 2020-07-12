# -*- coding:utf-8 _*-  
""" 
@file: utils.py 
@time: 2020-07-12 16:54
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from flask import request


def dispatch_request(fn_mapping: dict):
    fn = fn_mapping[request.method]
    return fn()


def row2dict(instance, *args, **kwargs):
    """
    convert SQLAlchemy instance to dict
    :param instance:
    :param args:
    :param kwargs:
    :rtype: dict
    """
    return {c.name: getattr(instance, c.name, None) for c in instance.__table__.columns}
