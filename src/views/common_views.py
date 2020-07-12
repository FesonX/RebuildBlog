# -*- coding:utf-8 _*-  
""" 
@file: common_views.py
@time: 2020-05-31 10:38
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from flask import render_template, request, jsonify, session, g, abort

from src import app
from src.controllers import request_validator
from src.dao import save_instances, get_article, get_articles
from src.enums import HttpMethod
from src.forms import ArticleForm, QueryForm
from src.models import ArticleTag, Article
from src.utils import dispatch_request, row2dict


@app.route('/')
def index():
    return render_template('index.html', cdn_domain='https://cdn.staticfile.org', title="FesonX's Blog")


@app.route('/editor', methods=['GET'])
def editor_manage():
    if request.method == 'GET':
        return render_template('article_manage.html', cdn_domain='https://cdn.staticfile.org', title="FesonX's Blog")


@app.route('/p/<int:id>', methods=['GET'], defaults={'id': -1})
def article_page(id):
    g.post_id = id
    return render_template('article_page.html', cdn_domain='https://cdn.staticfile.org', )


@app.route('/articles', defaults={'post_id': -1}, methods=['POST', 'GET'])
@app.route('/articles/<int:post_id>', methods=['POST', 'GET'])
def article_manage(post_id):
    g.post_id = post_id
    return dispatch_request({
        HttpMethod.GET: query_article,
        HttpMethod.POST: post_article
    })


@request_validator(ArticleForm)
def post_article():
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


def query_article():
    post_id = g.post_id
    if post_id != -1:
        article = get_article([Article.id == post_id])
        if article:
            article = row2dict(article)
            return jsonify({'msg': "Success", "data": article, "code": 200})
        else:
            abort(404)
    req_form: QueryForm = g.my_form
    articles = get_articles(page=req_form.page, per_page=req_form.per_page)
    if articles:
        articles = [row2dict(article) for article in articles]
    return jsonify({'msg': "Success", "data": articles, "code": 200})
