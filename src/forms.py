# -*- coding:utf-8 _*-  
""" 
@file: forms.py 
@time: 2020-06-07 15:22
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""

from wtforms import StringField, Form
from wtforms.validators import DataRequired


class ArticleForm(Form):
    title = StringField(label='title', validators=[DataRequired(message='Title is required')])
    column = StringField(label='column', validators=[DataRequired(message='Column is required')])
    author = StringField(label='author')
    body = StringField(label='body', validators=[DataRequired(message='Article body is required')])
    summary = StringField(label='summary')
    tags = StringField(label='tags')
