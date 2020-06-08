# -*- coding:utf-8 _*-  
""" 
@file: common_views.py
@time: 2020-05-31 10:38
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from flask import render_template, request, jsonify, session, g

from src import app
from src.controllers import request_validator
from src.dao import save_instances
from src.forms import ArticleForm
from src.models import ArticleTag, Article


@app.route('/')
def index():
    return render_template('index.html', cdn_domain='https://cdn.staticfile.org', title="FesonX's Blog")


@app.route('/editor', methods=['GET'])
def editor_manage():
    if request.method == 'GET':
        return render_template('article_manage.html', cdn_domain='https://cdn.staticfile.org', title="FesonX's Blog")


@app.route('/articles', methods=['POST'])
@request_validator(ArticleForm)
def article_manage():
    if request.method == 'POST':
        req_form: ArticleForm = g.my_form
        author = req_form.author.data or session.get('user_id')
        instances = list()
        article = Article(username=author, title=req_form.title.data,
                          body=req_form.body.data,
                          section=req_form.column.data, summary=req_form.summary.data or req_form.body.data[:50])
        instances.append(article)
        if req_form.tags.data:
            tags = [ArticleTag(tag=t, username=author) for t in req_form.tags.data]
            instances.extend(tags)
        save_instances(instances)
        return jsonify({"msg": "Success", "code": 200})
