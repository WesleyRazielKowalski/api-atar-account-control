#import flask
#from flask import jsonify
#from flask_http_response import success, result, error

from email_validator import validate_email, EmailNotValidError
import logging

class AccountControlObj():
    def insert(request_data):
        #if AccountControlObj.validate_insert():
        #    print("")
        return "insert"

    def update(request_data):
        #if AccountControlObj.validate_update(request_data):
        #    print("")
        return "update"

    def get(request_data):
        print("get")
        return "get"

    def validate_update(data):
        print("validate_update")
        return "validate_update"

    def validate_insert(data):
        print("validate_insert")
        return "validate_insert"


