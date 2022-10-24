from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development(object):
    DEBUG = True
    TESTING = False

class Testing(object):
    DEBUG = False
    TESTING = True

class Production(object):
    DEBUG = False
    TESTING = False

app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
