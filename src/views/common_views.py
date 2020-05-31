# -*- coding:utf-8 _*-  
""" 
@file: common_views.py
@time: 2020-05-31 10:38
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from flask import render_template
from src import app


@app.route('/')
def index():
    return render_template('base.html', cdn_domain='https://cdn.staticfile.org', title="FesonX's Blog")
