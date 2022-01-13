"""
This file have somes
configurations for the app
like the appid for the restapi

"""

from dotenv import load_dotenv
from os import environ

# charging
load_dotenv()

APPID = environ['APPID']
