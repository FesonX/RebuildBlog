# -*- coding:utf-8 _*-  
""" 
@file: config.py 
@time: 2020-05-24 16:12
@author:FesonX 
@contact: fesonx@foxmail.com
@site: github.com/FesonX 
@software: PyCharm 
"""

import os

# Get root path of project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Disable it to suppress warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
