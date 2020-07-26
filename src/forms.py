# -*- coding:utf-8 _*-  
""" 
@file: forms.py 
@time: 2020-06-07 15:22
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""

from wtforms import StringField, Form, IntegerField
from wtforms.validators import DataRequired


class ArticleForm(Form):
    title = StringField(label='title', validators=[DataRequired(message='Title is required')])
    column = StringField(label='column', validators=[DataRequired(message='Column is required')])
    author = StringField(label='author')
    body = StringField(label='body', validators=[DataRequired(message='Article body is required')])
    summary = StringField(label='summary')
    tags = StringField(label='tags')


class QueryForm(Form):
    author = StringField(label='author')
    title = StringField(label='article')
    column = StringField(label='column')
    page = IntegerField(label='page', default=0)
    per_page = IntegerField(label='per_page', default=20)
    tags = StringField(label='tags')
    create_time = IntegerField(label='create_time')
