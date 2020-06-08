# -*- coding:utf-8 _*-  
""" 
@file: controllers.py 
@time: 2020-05-31 10:34
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from functools import wraps

import werkzeug.datastructures
from flask import request, g, jsonify


def request_validator(form_class):
    def decorator(view_func):
        @wraps(view_func)
        def inner(*args, **kwargs):
            if request.method == 'GET':
                form_data = request.args
            else:
                if request.json:
                    print(request.json)
                    form_data = werkzeug.MultiDict(request.json)
                else:
                    form_data = request.form

            form = form_class(formdata=form_data)
            if not form.validate():
                return jsonify(code=400, message=form.errors), 400

            g.my_form = form
            return view_func(*args, **kwargs)

        return inner

    return decorator
