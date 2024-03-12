from flask import make_response
from src import controller as logic


class Menu(object):
    def _init_(self, session_id, user_response, msisdn=None, level=None):
        self.session_id = session_id  # M
        self.user_response = user_response  # M
        self.msisdn = msisdn  # M
        self.response_type = ""  # M
        self.level = level  # M

    def ussd_proceed(self, menu_text):
        pass

    def level(self):
        return self.level