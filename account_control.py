#import flask
#from flask import jsonify
#from flask_http_response import success, result, error
import logging
from flask import request
from account_validator import AccountValidator
#from account_datastore import AccountDatastore
from utils import messagesDefault

class AccountControlObj():
    def insert(request_data):
        try:
            if not request_data:
                raise str(messagesDefault.parameter_message_empty())

            if AccountControlObj.validate_insert():
                print("insert")
        except Exception as e:
            print(e)

    def update(request_data):
        try:
            if not request_data:
                raise str(messagesDefault.parameter_message_empty())

            if AccountControlObj.validate_update(request_data):
                print("validate_update")
        except Exception as e:
            print(str(e))

    def get(id):
        try:
            if not id:
                raise str(messagesDefault.parameter_message_empty())

            #result = AccountDatastore.get_register(id)
            print("get")
        except Exception as e:
            print(str(e))

    def validate_update(data):
        try:
            if not data:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_update")

        except Exception as e:
            print(str(e))

    def validate_insert(data):
        try:
            if not data:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_insert")
        except Exception as e:
            print(str(e))
