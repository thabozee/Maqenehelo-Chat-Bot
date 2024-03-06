import os
from dotenv import load_dotenv, find_dotenv

config_path = os.path.dirname(__file__)

dotenv_path = '.env'

load_dotenv(dotenv_path=find_dotenv(dotenv_path))

# META
meta_verification = {
    "WHATSAPP_TOKEN": os.getenv('WHATSAPP_TOKEN'),
    "VERIFY_TOKEN": os.getenv('VERIFY_TOKEN'),
}

