from google.cloud import datastore, storage
import os

class AccountDatastore():
    def set_keystore():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.path.realpath(__file__))+"/key_datastore.json"

    def insert_register(account_obj):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            with client.transaction():
                key = client.allocate_ids(client.key('users'), 1)[0]
                my_id = key.id

                entity = datastore.Entity(key=key)
                entity.update(account_obj.get_datastore())
                client.put(entity)

                return my_id
        except Exception as e:
            return ("Erro ao inserir novo registro no datastore!")

    def update_register(account_obj):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            complete_key = client.key("users", int(account_obj.id))
            entity = datastore.Entity(key=complete_key)
            entity.update(account_obj.get_datastore())
            client.put(entity)
            return entity
        except Exception as e:
            return ("Erro ao alterar registro no datastore!")

    def get_register(id):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            query = client.query(kind="users")
            complete_key = client.key("users", int(id))
            query.key_filter(complete_key, "=")
            return_list = list(query.fetch())
            return return_list
        except Exception as e:
            return ("Erro ao buscar registro no datastore!")

    def email_registered(email):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            query = client.query(kind="users")
            query.add_filter("email", "=", str(email))
            register = list(query.fetch())
            if len(register):
                return True, register
            else:
                return False, 0
        except Exception as e:
            return ("Erro ao validar email cadastrado no datastore!")

    def document_registered(document):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            query = client.query(kind="users")
            query.add_filter("document", "=", str(document))
            register = list(query.fetch())
            if len(register):
                return True, register
            else:
                return False, 0
        except Exception as e:
            return ("Erro ao validar documento cadastrado no datastore!")





