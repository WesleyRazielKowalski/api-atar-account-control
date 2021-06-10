import logging
from email_validator import validate_email, EmailNotValidError
from utils import messagesDefault
import re
from datetime import datetime
from dateutil import relativedelta
from validate_email import validate_email
from account_datastore import AccountDatastore

class AccountValidator():
    def validate_document(document):
        try:
            if not document:
                raise str(messagesDefault.parameter_message_empty())

            from validate_docbr import CPF, CNPJ
            if len(AccountValidator().clean_characters_document(document)) == 11:
                cpf = CPF()
                return cpf.validate(AccountValidator().clean_characters_document(document))
            elif len(AccountValidator().clean_characters_document(document)) == 14:
                cnpj = CNPJ()
                return cnpj.validate(AccountValidator().clean_characters_document(document))

            return False
        except Exception as e:
            print(str(e))

    def validate_phone(phone):
        try:
            if not phone:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_phone")
        except Exception as e:
            print(str(e))

    def validate_email(email):
        try:
            if not email:
                raise str(messagesDefault.parameter_message_empty())

            return validate_email(email)
        except EmailNotValidError as e:
            print(e)

    def validate_birthdate_older_eighteen(date):
        try:
            if not date:
                raise str(messagesDefault.parameter_message_empty())

            date_date = datetime.strptime(AccountValidator().formating_birthdate(date), '%d/%m/%Y').date()
            date_now = datetime.now().date()
            years_old = relativedelta.relativedelta(date_now, date_date).years

            if years_old >= 18:
                return True
            else:
                return False
        except Exception as e:
            print(str(e))

    def validate_exists_registered_email(id_account_currency, email, is_put = True):
        try:
            if not email:
                raise str(messagesDefault.parameter_message_empty())

            result = False
            register = AccountDatastore.email_registered(email)
            if register[0]:
                if not is_put:
                    result = True
                else:
                    if int(register[1][0].id) != int(id_account_currency) and is_put:
                        result = True


            return result
        except Exception as e:
            print(str(e))

    def validate_exists_registered_document(id_account_currency, document, is_put = True):
        try:
            if not document:
                raise str(messagesDefault.parameter_message_empty())

            result = False
            register = AccountDatastore.document_registered(document)
            if register[0]:
                if not is_put:
                    result = True
                else:
                    if int(register[1][0].id) != int(id_account_currency) and is_put:
                        result = True

            return result
        except Exception as e:
            print(str(e))

    def validate_exists_registered_id(id):
        try:
            if not id:
                raise str(messagesDefault.parameter_message_empty())

            result = False
            register = AccountDatastore.get_register(id)
            if register:
                if register[0]:
                    if int(register[0].id) == int(id):
                        result = True

            return result
        except Exception as e:
            print(str(e))

    def formating_phone(self, phone):
        phone_clean = str(self.clean_characters_phone(phone))
        if len(phone_clean) == 8:
            return '{}-{}'.format(phone_clean[:4], phone_clean[4:8])
        elif len(phone_clean) == 9:
            return '{}-{}'.format(phone_clean[:5], phone_clean[5:9])
        elif len(phone_clean) == 10:
            return '({}) {}-{}'.format(phone_clean[:2], phone_clean[2:6], phone_clean[6:10])
        elif len(phone_clean) == 11 and (phone_clean[:1]) == "0":
            return '({}) {}-{}'.format(phone_clean[:3], phone_clean[3:7], phone_clean[7:11])
        elif len(phone_clean) == 11:
            return '({}) {}-{}'.format(phone_clean[:2], phone_clean[2:7], phone_clean[7:11])
        elif len(phone_clean) == 12:
            return '({}) {}-{}'.format(phone_clean[:3], phone_clean[3:8], phone_clean[8:12])

    def formating_document(self, document):
        document_clean = str(self.clean_characters_document(document))
        if len(document_clean) == 11:
            return '{}.{}.{}-{}'.format(document_clean[:3], document_clean[3:6], document_clean[6:9], document_clean[9:])
        elif len(document_clean) == 14:
            return '{}.{}.{}/{}-{}'.format(document_clean[:2], document_clean[2:5], document_clean[5:8], document_clean[8:12], document_clean[12:14])

    def formating_birthdate(self, birthdate):
        birthdate_clean = str(self.clean_characters_birthdate(birthdate))
        if len(birthdate_clean) == 6:
            return '{}/{}/{}'.format(birthdate_clean[:2], birthdate_clean[2:4], birthdate_clean[4:6])
        elif len(birthdate_clean) == 8:
            return '{}/{}/{}'.format(birthdate_clean[:2], birthdate_clean[2:4], birthdate_clean[4:8])

    def clean_characters_birthdate(self, birthdate):
        return re.sub('[^0-9]', '', birthdate)

    def clean_characters_document(self, document):
        return re.sub('[^0-9]', '', document)

    def clean_characters_phone(self, phone):
        return re.sub('[^0-9]', '', phone)