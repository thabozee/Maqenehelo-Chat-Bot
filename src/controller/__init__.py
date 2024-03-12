from src.model.hanlde_messaages.redis import ChatbotRedisHandler


def set_user_state(msisdn, state):
    chat_bot_r_handler_obj = ChatbotRedisHandler()
    chat_bot_r_handler_obj.set_user_state(user_id=msisdn, state=state)


# check if session exists
def check_if_state_exists(msisdn):
    chat_bot_r_handler_obj = ChatbotRedisHandler()
    user_state = chat_bot_r_handler_obj.get_user_state(user_id=msisdn)
    return user_state


def set_deceased_status(msisdn, status):
    chat_bot_r_handler_obj = ChatbotRedisHandler()
    chat_bot_r_handler_obj.set_deceased_status(user_id=msisdn, status=status)


def get_deceased_status(msisdn):
    chat_bot_r_handler_obj = ChatbotRedisHandler()
    deceased_status = chat_bot_r_handler_obj.get_deceased_status(user_id=msisdn)
    return deceased_status
