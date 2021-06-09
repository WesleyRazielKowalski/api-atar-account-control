#import flask
#from flask import jsonify
#from flask_http_response import success, result, error
import logging
from flask import request
from account_validator import AccountValidator
from account_datastore import AccountDatastore
from account_object import AccountObject
from utils import messagesDefault
from flask import json, Response

class AccountControlObj():

    def control_insert(request_data):
        try:
            if not request_data:
                raise str(messagesDefault.parameter_message_empty())

            account_obj = AccountObject(request_data)
            if AccountControlObj.validate_control_insert(account_obj):
                return AccountDatastore.insert_register(account_obj)
        except Exception as e:
            return e

    def control_update(request_data, id):
        try:
            if (not request_data) or (not id):
                raise str(messagesDefault.parameter_message_empty())

            account_obj = AccountObject(request_data, id)
            if AccountControlObj.validate_control_update(account_obj):
                return AccountDatastore.update_register(account_obj)
        except Exception as e:
            return e

    def control_get(id):
        try:
            if not id:
                raise str(messagesDefault.parameter_message_empty())

            list_datastore = AccountDatastore.get_register(id)
            register = AccountObject()
            register.entry_data_with_datastore(list_datastore[0])
            return register.get_json()

        except Exception as e:
            return e

    def validate_control_insert(account_obj):
        return True
        try:
            if not account_obj:
                raise str(messagesDefault.parameter_message_empty())



        except Exception as e:
            return e

    def validate_control_update(account_obj):
        return True
        try:
            if not account_obj:
                raise str(messagesDefault.parameter_message_empty())



        except Exception as e:
            return e
