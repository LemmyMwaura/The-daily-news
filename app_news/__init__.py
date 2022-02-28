from flask import Flask
from config import config_options

app = Flask(__name__)
from app_news import views
from app_news import errors