import logging
from email_validator import validate_email, EmailNotValidError
from utils import messagesDefault

class AccountValidator():
    def validate_cpf(cpf):
        try:
            if not cpf:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_cpf")
        except Exception as e:
            print(str(e))

    def validate_email(email):
        try:
            #if not email:
                #raise "Parâmetro de método não informado")

            valid = validate_email(email)
            # email = valid.email
        except EmailNotValidError as e:
            print(e)

    def validate_phone(phone):
        try:
            if not phone:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_phone")
        except Exception as e:
            print(str(e))

    def validate_bithdate_older_eighteen(bithdate):
        try:
            if not bithdate:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_bithdate_older_eighteen")
        except Exception as e:
            print(str(e))

    def exists_registered_email(email):
        try:
            if not email:
                raise str(messagesDefault.parameter_message_empty())

            print("registered_email")
        except Exception as e:
            print(str(e))

    def exists_registered_cpf(cpf):
        try:
            if not cpf:
                raise str(messagesDefault.parameter_message_empty())

            print("exists_registered_cpf")
        except Exception as e:
            print(str(e))