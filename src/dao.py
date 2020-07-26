# -*- coding:utf-8 _*-  
""" 
@file: dao.py 
@time: 2020-06-07 10:21
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from src.models import Article
from src import db
from loguru import logger
from collections import Sequence


def update():
    try:
        db.session.commmit()
    except Exception as e:
        db.session.rollback()
        logger.exception(e)


def save_instances(instances: Sequence):
    try:
        db.session.bulk_save_objects(instances)
        db.session.commit()
    except Exception as e:
        logger.exception(e)


def get_articles(query_conditions, fields=None, page: int = 0, per_page: int = 20):
    if fields:
        fields = [getattr(Article, field) for field in fields]
    base_query = db.session.query(fields or Article)
    if query_conditions:
        base_query = base_query.filter(*query_conditions)
    return base_query.offset(page).limit(per_page)


def get_article(query_conditions, fields=None):
    if fields:
        fields = [getattr(Article, field) for field in fields]
    return db.session.query(fields or Article).filter(*query_conditions).first()


def get_columns():
    return db.session.query(Article.section.distinct()).all()
