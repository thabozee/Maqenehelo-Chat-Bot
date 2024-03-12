# check session
from src import controller as logic


def navigation(msisdn, message):
    # get session
    greetings = ["hi", "hello", "greetings"]
    state = logic.check_if_state_exists(msisdn)

    if state is None and message.lower() in greetings:
        return "intitial_contact"
