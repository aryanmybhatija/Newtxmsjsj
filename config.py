import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7755241058:AAGqRdK0OXThnu0W26F82uKGr6PjCaBvza8"
    # Telegram API ki ID
    API_ID = 24602445
    # Telegram API ki hash key
    API_HASH = "180adef97e5d2f8a246f59280ce625b5"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '6890400066,5744263553'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://user:user1@cluster0.sp0pitj.mongodb.net/"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002561868621
    # Authentication log channel ki ID
    AUTH_LOG = -1002594448328
    # Hit log channel ki ID
    HIT_LOG = -1002561868621
    # DRM dump channel ki ID
    DRM_DUMP = -1002561868621
    # Main channel ki ID
    CHANNEL = -1002594448328
    # Channel ka link
    CH_URL = "https://t.me/+jbgZyPCEyYI2ZTdl"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Contact_adminSbot"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

