import logging
from email_validator import validate_email, EmailNotValidError
from utils import messagesDefault
import re

class AccountValidator():
    def validate_document(document):
        try:
            if not document:
                raise str(messagesDefault.parameter_message_empty())

            print("validate_document")
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

    #def clean_characters_birthdate(self, birthdate):

        #internal_phone = phone
        #all = string.maketrans('','')
        #nodigs = all.translate(all, string.digits)
        #internal_phone.translate(all, nodigs)
        #return internal_phone


    # def exists_registered_email(email):
    #     try:
    #         if not email:
    #             raise str(messagesDefault.parameter_message_empty())
    #
    #         print("registered_email")
    #     except Exception as e:
    #         print(str(e))
    #
    # def exists_registered_cpf(cpf):
    #     try:
    #         if not cpf:
    #             raise str(messagesDefault.parameter_message_empty())
    #
    #         print("exists_registered_cpf")
    #     except Exception as e:
    #         print(str(e))