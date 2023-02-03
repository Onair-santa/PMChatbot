import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN","")
    API_ID = int(os.environ.get("API_ID",""))
    API_HASH = os.environ.get("API_HASH","")
    ADMIN = int(os.environ.get("ADMIN",""))
