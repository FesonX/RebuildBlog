# -*- coding:utf-8 _*-
""" 
@file: app.py 
@time: 2020-05-18 23:34
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""
from src import app


@app.route('/')
def test():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
