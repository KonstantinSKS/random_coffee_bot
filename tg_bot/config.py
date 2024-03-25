import os
import logging

from dotenv import load_dotenv

load_dotenv()

"""Logging levels"""
DEBUG = os.getenv('DEBUG', 'False') == 'True'

"""Tokens"""
BOT_TOKEN = os.getenv('BOT_TOKEN')

"""Domain"""
ALLOWED_DOMAIN = os.getenv('ALLOWED_DOMAIN')

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

"""Настройки для рассылки"""
MEETING_DAY: str = 'sun'  # дни недели: mon,tue,wed,thu,fri,sat,sun
MEETING_TIME: int = 15
