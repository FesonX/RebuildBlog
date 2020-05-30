# -*- coding:utf-8 _*-  
""" 
@file: setup.py 
@time: 2020-05-30 14:57
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from loguru import logger

from src import db
from src.models import Article, ArticleComment, ArticleTag, UserAuth, UserInfo


def set_server_side_on_update(table):
    sql = 'ALTER TABLE %s CHANGE `update_time` `update_time` datetime ' \
          'DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP' % table.__tablename__
    rtn = db.session.execute(sql)
    return rtn


if __name__ == '__main__':
    if any((t.__tablename__ not in db.engine.table_names() for t in
            (Article, ArticleComment, ArticleTag, UserAuth, UserInfo))):
        logger.info('Begin create table...')
        db.create_all()
        logger.info('Table created.')

    logger.info('Set server-side update_time ON UPDATE')
    for t in (Article, ArticleComment, ArticleTag, UserAuth, UserInfo):
        set_server_side_on_update(t)
    logger.info('Tables in current db: %r' % db.engine.table_names())
