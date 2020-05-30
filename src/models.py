# -*- coding:utf-8 _*-  
""" 
@file: models.py 
@time: 2020-05-18 23:35
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from flask_login import UserMixin
from sqlalchemy import func, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from werkzeug.security import generate_password_hash, check_password_hash

from src import db

# Detail MySQL on SQLAlchemy, ref: https://docs.sqlalchemy.org/en/13/dialects/mysql.html
COMMON_TABLE_SETTINGS = {
    'mysql_charset': 'utf8mb4',
    'mysql_engine': 'InnoDB'
}


class BaseModel(db.Model):
    __abstract__ = True
    __tablename__ = ''
    # Configuration Document: https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/table_config.html
    __table_args__ = ''
    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, server_default=func.now())
    # This is a client-side update trigger.
    # Will not be reflect on db.
    update_time = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        pass


class UserAuth(BaseModel, UserMixin):
    __tablename__ = 'tbl_user_auth'
    __table_args__ = (
        db.Index('ix_user_auth_username', 'username'),
        db.Index('ix_user_auth_email', 'email'),
        db.UniqueConstraint('username'),
        COMMON_TABLE_SETTINGS
    )
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<{name} {id} {username} {email}>'.format(name=self.__name__, id=self.id, username=self.username,
                                                         email=self.email)


class UserInfo(BaseModel):
    __tablename__ = 'tbl_user_info'
    __table_args__ = (
        db.Index('ix_user_info_username', 'username'),
        db.UniqueConstraint('username'),
        COMMON_TABLE_SETTINGS
    )
    username = db.Column(db.String(64), nullable=False)
    country = db.Column(db.String(8), server_default='')
    city = db.Column(db.String(32), server_default='')
    avatar = db.Column(db.String(128), server_default='')
    intro = db.Column(db.String(128), server_default='')

    def __repr__(self):
        return '<{name} {id} {username} {country}>'.format(name=self.__name__, id=self.id, username=self.username,
                                                           country=self.country)


class Article(BaseModel):
    __tablename__ = 'tbl_article'
    __table_args__ = (
        db.Index('ix_article_username', 'username'),
        db.Index('ix_article_title', 'title'),
        db.Index('ix_article_section', 'section'),
        COMMON_TABLE_SETTINGS
    )
    username = db.Column(db.String(64), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.TEXT, nullable=False)
    slug = db.Column(db.String(256), nullable=False)
    section = db.Column(db.String(64), server_default='')

    def __repr__(self):
        return '<{name} {id} {username} {title}>'.format(name=self.__name__, id=self.id, username=self.username,
                                                         title=self.title)


class ArticleTag(BaseModel):
    __tablename__ = 'tbl_tag'
    __table_args__ = (
        db.Index('ix_tag_tag', 'tag'),
        db.Index('ix_tag_title', 'title'),
        COMMON_TABLE_SETTINGS
    )
    tag = db.Column(db.String(32), nullable=False, server_default='')
    username = db.Column(db.String(64), server_default='')
    title = db.Column(db.String(128), nullable=False, server_default='')

    def __repr__(self):
        return '<{name} {id} {tag} {username}>'.format(name=self.__name__, id=self.id, tag=self.tag,
                                                       username=self.username)


class ArticleComment(BaseModel):
    __tablename__ = 'tbl_comment'
    __table_args__ = (
        db.Index('ix_comment', 'body'),
        COMMON_TABLE_SETTINGS
    )
    username = db.Column(db.String(64), nullable=False, server_default='')
    body = db.Column(db.String(256), nullable=False, server_default='')
    ip = db.Column(INTEGER(unsigned=True), server_default=text('0'))
    country_code = db.Column(db.String(8), server_default='')

    def __repr__(self):
        return '<{name} {id} {username} {body}>'.format(name=self.__name__, id=self.id, username=self.username,
                                                        body=self.body[:16])

