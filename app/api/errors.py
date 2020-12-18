# 为所有客户端生成适当响应的一种方法是，在错误处理程序中根据客户端请求的格式改写 响应，这种技术称为内容协商。

from flask import jsonify
from app.exceptions import ValidationError
from . import api


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.headers['WWW-Authenticate'] = 'Bearer'
    response.status_code = 401
    return response


def token_missing(message):
    response = jsonify({'error': 'token_missing', 'message': message})
    response.headers['WWW-Authenticate'] = 'Bearer'
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
