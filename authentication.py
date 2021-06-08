# -*- coding: utf-8 -*-
import json
import logging
import base64
ACCESS_TOKEN = "Basic 1cbde8c01abc25f39f18d2bad8a6ac2480c3b42f"


class Authentication(object):

    @staticmethod
    def check_can_access(token_authentication):
        try:
            if token_authentication == Authentication.get_token_encode():
                return True
        except Exception as e:
            logging.exception(e)
            pass
        return False

    @staticmethod
    def get_token_encode():
        username = "wesley"
        password = "kowalski"
        auth_token_byte = str(username + ":" + password).encode("utf-8")
        return "Basic "+base64.b64encode(auth_token_byte).decode()