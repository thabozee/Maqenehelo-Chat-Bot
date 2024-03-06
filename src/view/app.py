# framework
from flask import Flask, make_response, json, request
from flask_cors import CORS

# blueprints
from src.view.blueprints.handle_messages import handle_messages_bp

whatsapp_webhook = Flask(__name__)
CORS(app=whatsapp_webhook)


def build():
    with whatsapp_webhook.app_context():
        whatsapp_webhook.register_blueprint(blueprint=handle_messages_bp)

        @whatsapp_webhook.route("/", methods=["GET"])
        def test():
            print(f"\n{whatsapp_webhook.url_map}\n")
            return make_response("We're up!!!")

        return whatsapp_webhook
