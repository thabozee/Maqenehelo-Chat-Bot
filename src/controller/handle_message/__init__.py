from flask import jsonify
import requests
import config as env
from src.controller.handle_message import menu_navigation
import os


# download the media file from the media url
def download_media_file(media_url, filename, location):
    headers = {
        "Authorization": f"Bearer {env.meta_verification['WHATSAPP_TOKEN']}",
    }
    response = requests.get(media_url, headers=headers)
    if response.status_code == 200:
        if not os.path.exists(location):
            os.makedirs(location)

        full_path = os.path.join(location, filename)
        with open(full_path, 'wb') as f:
            f.write(response.content)
        print(f"Audio file downloaded successfully as {filename}")
    else:
        print("Failed to download the audio file.")


# get the media url from the media id
def get_media_url(media_id):
    headers = {
        "Authorization": f"Bearer {env.meta_verification['WHATSAPP_TOKEN']}",
    }
    url = f"https://graph.facebook.com/v16.0/{media_id}/"
    response = requests.get(url, headers=headers)
    print(f"media id response: {response.json()}")
    return response.json()["url"]


# send the response as a WhatsApp message back to the user
def send_whatsapp_message(from_number, t_message):
    headers = {
        "Authorization": f"Bearer {env.meta_verification['WHATSAPP_TOKEN']}",
        "Content-Type": "application/json",
    }
    url = "https://graph.facebook.com/v15.0/" + "249525811575126" + "/messages"
    data = {
        "messaging_product": "whatsapp",
        "to": from_number,
        "type": "template",
        "template": {"name": t_message, "language": {"code": "en_US"}},
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"whatsapp message response: {response.json()}")
    response.raise_for_status()


# handle WhatsApp messages of different type
def handle_whatsapp_message(body):
    message = body["entry"][0]["changes"][0]["value"]["messages"][0]

    if message["type"] == "text":

        message_body = message["text"]["body"]
        session = message["from"]
        nav = menu_navigation.navigation(session, message_body)

        send_whatsapp_message(session, t_message=nav)

    elif message["type"] == "button":

        message_body = message["button"]["payload"].lower()
        session = message["from"]
        nav = menu_navigation.navigation(session, message_body)

        send_whatsapp_message(session, t_message=nav)

    elif message["type"] == "audio":
        media_url = get_media_url(media_id=body['entry'][0]['changes'][0]['value']['messages'][0]['audio']['id'])
        sender = filename = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
        file_type = "." + \
                    body['entry'][0]['changes'][0]['value']['messages'][0]['audio']['mime_type'].split("/")[1].split(
                        ";")[0]
        download_media_file(media_url, filename + "_" + body['entry'][0]['changes'][0]['value']['messages'][0]['audio'][
            'id'] + file_type, sender)

    elif message["type"] == "image":
        media_url = get_media_url(media_id=body['entry'][0]['changes'][0]['value']['messages'][0]['image']['id'])
        sender = filename = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
        file_type = "." + \
                    body['entry'][0]['changes'][0]['value']['messages'][0]['image']['mime_type'].split("/")[1].split(
                        ";")[0]
        download_media_file(media_url, filename + "_" + body['entry'][0]['changes'][0]['value']['messages'][0]['image'][
            'id'] + file_type, sender)

    elif message["type"] == "document":
        media_url = get_media_url(media_id=body['entry'][0]['changes'][0]['value']['messages'][0]['document']['id'])
        filename = body['entry'][0]['changes'][0]['value']['messages'][0]['document']['id'] + "_" + body['entry'][0]['changes'][0]['value']['messages'][0]['document']['filename'] \

        sender = body['entry'][0]['changes'][0]['value']['messages'][0]['from']
        download_media_file(media_url, filename, sender)


# handle incoming webhook messages
def handle_message(request):
    # Parse Request body in json format
    body = request.get_json()
    print(f"request body: {body}")

    try:
        # info on WhatsApp text message payload:
        # https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples#text-messages
        if body.get("object"):
            if (
                    body.get("entry")
                    and body["entry"][0].get("changes")
                    and body["entry"][0]["changes"][0].get("value")
                    and body["entry"][0]["changes"][0]["value"].get("messages")
                    and body["entry"][0]["changes"][0]["value"]["messages"][0]
            ):
                handle_whatsapp_message(body)
            return jsonify({"status": "ok"}), 200
        else:
            # if the request is not a WhatsApp API event, return an error
            return (
                jsonify({"status": "error", "message": "Not a WhatsApp API event"}),
                404,
            )
    # catch all other errors and return an internal server error
    except Exception as e:
        print(f"unknown error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500


# Required webhook verification for WhatsApp
# info on verification request payload:
# https://developers.facebook.com/docs/graph-api/webhooks/getting-started#verification-requests
def verify(request):
    # Parse params from the webhook verification request
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    print(mode)
    print(token)
    print(challenge)
    # Check if a token and mode were sent
    if mode and token:
        # Check the mode and token sent are correct
        if mode == "subscribe" and token == env.meta_verification['VERIFY_TOKEN']:
            # Respond with 200 OK and challenge token from the request
            print("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            # Responds with '403 Forbidden' if verify tokens do not match
            print("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verification failed"}), 403
    else:
        # Responds with '400 Bad Request' if verify tokens do not match
        print("MISSING_PARAMETER")
        return jsonify({"status": "error", "message": "Missing parameters"}), 400
