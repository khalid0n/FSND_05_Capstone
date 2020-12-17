import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code



#@TODO class AuthError(Exception):

#@TODO def get_token_header():



#@TODO def check_permission(permission, payload):


#@TODO def verify_decode_jwt(token):

#@TODO def requires_auth(permission=''):