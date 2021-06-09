from dns.rdtypes.CH.A import A

from account_validator import AccountValidator

class AccountObject():
    id = 0
    birth_date = ""
    document = ""
    email = ""
    full_name = ""
    phone = ""

    def __init__(self, request_data_internal = None, id = 0):
        if request_data_internal:
            self.id = 0 if id == 0 else id
            self.birth_date = str(AccountValidator().clean_characters_birthdate(request_data_internal.json["birthDate"]))
            self.document = str(AccountValidator().formating_document(request_data_internal.json["document"]))
            self.email = str(request_data_internal.json["email"])
            self.full_name = str(request_data_internal.json["fullName"])
            self.phone = str(AccountValidator().formating_phone(request_data_internal.json["phone"]))

    def convert_request_into_account_object(self, request_data_internal, id = 0):
        if request_data_internal:
            self.id = 0 if id == 0 else id
            self.birth_date = str(AccountValidator().clean_characters_birthdate(request_data_internal.json["birthDate"]))
            self.document = str(AccountValidator().formating_document(request_data_internal.json["document"]))
            self.email = str(request_data_internal.json["email"])
            self.full_name = str(request_data_internal.json["fullName"])
            self.phone = str(AccountValidator().formating_phone(request_data_internal.json["phone"]))

    def entry_data_with_datastore(self, data_datastore):
        self.id = data_datastore.id
        self.birth_date = str(AccountValidator().clean_characters_birthdate(data_datastore["birthDate"]))
        self.document = str(AccountValidator().clean_characters_document(data_datastore["document"]))
        self.email = str(data_datastore["email"])
        self.full_name = str(data_datastore["fullName"])
        self.phone = str(AccountValidator().clean_characters_phone(data_datastore["phone"]))

    def get_json(self):
        data = {
            'id': int(self.id),
            'birthDate': str(AccountValidator().formating_birthdate(self.birth_date)),
            'document': str(AccountValidator().formating_document(self.document)),
            'email': str(self.email),
            'fullName': str(self.full_name),
            'phone': str(AccountValidator().formating_phone(self.phone)),
        }
        return data
    def get_json_without_id(self):
        data = {
            'birthDate': str(AccountValidator().formating_birthdate(self.birth_date)),
            'document': str(AccountValidator().formating_document(self.document)),
            'email': str(self.email),
            'fullName': str(self.full_name),
            'phone': str(AccountValidator().formating_phone(self.phone)),
        }
        return data
