# check session
from src import controller as logic


def navigation(msisdn, message):
    # get session
    greetings = ["hi", "hello", "greetings"]
    state = logic.check_if_state_exists(msisdn)

    if state is None and message.lower() in greetings:  # greetings
        logic.set_user_state(msisdn, "initial_contact")
        return "initial_contact"

    if state == "initial_contact":
        if message.lower() == "1":
            logic.set_user_state(msisdn, "policy_holder")
            return "policy_holder"

    if state == "policy_holder":
        # count number of documents
        if message.lower() in ["policyholder", "beneficiary"]:
            logic.set_user_state(msisdn, "cause_of_death")
            return "cause_of_death"

    if state == "cause_of_death":
        logic.set_user_state(msisdn, "item_upload_acknowledgement")

        if message.lower() == "natural death":
            return "documents_to_upload_policy_holder_and_natural_death"

        if message.lower() == "accidental death":
            return "documents_to_upload_policy_holder_and_accidental_death"

    if state == "documents_to_upload_policy_holder_and_natural_death":
        return "item_upload_acknowledgement"

    if state == "documents_to_upload_policy_holder_and_accidental_death":
        return "item_upload_acknowledgement"

    if state == "item_upload_acknowledgement":
        if message.lower() == "1":
            return "item_upload_acknowledgement"
