# 可以添加带有版本号的包, 让应用同时支持两个版本的 api
# API 蓝本, 各资源在不同的模块中实现

from flask import Blueprint
api = Blueprint('api_bp', __name__)
from . import authentication, posts, users, comments, errors