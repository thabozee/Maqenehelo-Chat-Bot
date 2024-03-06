from flask import Blueprint, make_response, json, request
from src.controller.handle_message import handle_message
from src.controller.handle_message import verify
handle_messages_bp = Blueprint(name="handle_messages_bp", import_name=__name__, url_prefix="/handle_messages/webhook")


@handle_messages_bp.route("/", methods=["POST"])
def handle_message_fn():
    if request.method == "GET":
        return verify(request)
    elif request.method == "POST":
        return handle_message(request)




