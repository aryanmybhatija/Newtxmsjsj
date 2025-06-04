import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = ""
    # Telegram API ki ID
    API_ID = 28964382
    # Telegram API ki hash key
    API_HASH = "c552befc21408d4ef175a66cb44cc33c"
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
    OWNER = "https://t.me/Sonuporsa"
    # Thumbnail image ka URL
    THUMB_URL = "https://myappme.shop/img/file_224.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

