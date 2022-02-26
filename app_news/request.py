import os
import requests
from .models import Articles

api_key = os.environ.get('NEWS_API_KEY')

def get_articles():
    url = f'https://newsapi.org/v2/everything?q=bitcoin&apiKey={api_key}'
    response = requests.get(url)
    news_dict = response.json()

    return news_dict['articles']

def process_articles():
    articles_list = []
    articles = get_articles()
    for article in articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urltoImage = article.get('urltoImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        news_object = Articles(author,title,description,url,urltoImage,publishedAt,content)
        articles_list.append(news_object)

    return articles_list

process_articles()