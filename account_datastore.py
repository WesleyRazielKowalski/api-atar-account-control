from google.cloud import datastore, storage
import os

class AccountDatastore():
    def set_keystore():
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/wesley/workspace/Me/POC/atar/key_datastore.json"

    def insert_register(account_obj):
        AccountDatastore.set_keystore()
        client = datastore.Client()
        try:
            with client.transaction():
                key = client.allocate_ids(client.key('users'), 1)[0]
                my_id = key.id

                entity = datastore.Entity(key=key)
                entity.update(account_obj.get_json_without_id())
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
            entity.update(account_obj.get_json())
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
            return ("Erro ao alterar registro no datastore!")
            #client = datastore.Client()
            # query = client.query(kind="users")
            # query.filter('key =', str(id))
            # items = list(query.fetch())
            # list_return = []
            # for item in items:
            #    item_item =
        except Exception as e:
            return ("Erro ao buscar registro no datastore!")




