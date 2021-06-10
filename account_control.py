#import flask
#from flask import jsonify
#from flask_http_response import success, result, error
import logging
from flask import request, json, Response
from account_validator import AccountValidator
from account_datastore import AccountDatastore
from account_object import AccountObject
from utils import messagesDefault

class AccountControlObj():

    def control_insert(request_data):
        try:
            if not request_data:
                raise str(messagesDefault.parameter_message_empty())

            account_obj = AccountObject(request_data)
            validate = AccountControlObj.validate_control_insert(account_obj)
            if validate[0] == True:
                return {"id" : AccountDatastore.insert_register(account_obj)}, 200
            else:
                return {"erro": str(validate[0])}, validate[1]
        except Exception as e:
            return e

    def control_update(request_data, id):
        try:
            if (not request_data) or (not id):
                raise str(messagesDefault.parameter_message_empty())

            account_obj = AccountObject(request_data, id)
            validate = AccountControlObj.validate_control_update(account_obj)
            if validate[0] == True:
                account_obj.entry_data_with_datastore(AccountDatastore.update_register(account_obj))
                return {"data": account_obj.get_json()}, 201
            else:
                return {"erro": str(validate[0])}, validate[1]
        except Exception as e:
            return e

    def control_get(id):
        try:
            if not id:
                raise str(messagesDefault.parameter_message_empty())

            validate = AccountControlObj.validate_control_get(id)
            if validate[0] == True:
                list_datastore = AccountDatastore.get_register(id)
                register = AccountObject()
                register.entry_data_with_datastore(list_datastore[0])
                return {"data": register.get_json()}, 200
            else:
                return {"erro": str(validate[0])}, validate[1]

        except Exception as e:
            return e

    def validate_control_insert(account_obj):
        try:
            if not account_obj:
                raise str(messagesDefault.parameter_message_empty())

            if not AccountValidator.validate_birthdate_older_eighteen(account_obj.birth_date):
                return ("Data de nascimento menor que 18 anos"), 400

            if not AccountValidator.validate_document(account_obj.document):
                return ("Documento inválido"), 400

            if not AccountValidator.validate_email(account_obj.email):
                return ("E-mail inválido"), 406

            if AccountValidator.validate_exists_registered_email(account_obj.id, account_obj.email, False):
                return ("E-mail já cadastrado"), 409

            if AccountValidator.validate_exists_registered_document(account_obj.id, account_obj.document, False):
                return ("Documento já cadastrado"), 400

            return True, 200
        except Exception as e:
            return e

    def validate_control_update(account_obj):
        try:
            if not account_obj:
                raise str(messagesDefault.parameter_message_empty())

            if not AccountValidator.validate_exists_registered_id(account_obj.id):
                return ("Id não cadastrado"), 400

            if not AccountValidator.validate_birthdate_older_eighteen(account_obj.birth_date):
                return ("Data de nascimento menor que 18 anos"), 400

            if not AccountValidator.validate_document(account_obj.document):
                return ("Documento inválido"), 400

            if not AccountValidator.validate_email(account_obj.email):
                return ("E-mail inválido"), 406

            if AccountValidator.validate_exists_registered_email(account_obj.id, account_obj.email):
                return ("E-mail já cadastrado"), 409

            if AccountValidator.validate_exists_registered_document(account_obj.id, account_obj.document):
                return ("Documento já cadastrado"), 400

            return True, 200
        except Exception as e:
            return e

    def validate_control_get(id):
        try:
            if not id:
                raise str(messagesDefault.parameter_message_empty())

            if not AccountValidator.validate_exists_registered_id(id):
                return ("Id não cadastrado"), 400

            return True, 200
        except Exception as e:
            return e
