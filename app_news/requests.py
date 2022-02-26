import os
import requests

api_key = os.environ.get('NEWS_API_KEY')
url = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=api_key'