import os
import requests
from .models import Articles, Categories, News_Source, All_news_sources

api_key = os.environ.get('NEWS_API_KEY')

def get_articles():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
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
        urltoImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        news_object = Articles(author,title,description,url,urltoImage,publishedAt,content)
        articles_list.append(news_object)

    return articles_list

def get_categories(category):
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
    response = requests.get(url)
    categories_dict = response.json()

    return categories_dict['articles']

def process_categories(category):
    category_list = []
    categoties = get_categories(category)
    for article in categoties:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urltoImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        category_object = Categories(author,title,description,url,urltoImage,publishedAt,content)
        category_list.append(category_object)

    return category_list

def get_news_sources(news_source):
    url = f'https://newsapi.org/v2/top-headlines?sources={news_source}&apiKey={api_key}'
    response = requests.get(url)
    news_source_dict = response.json()

    return news_source_dict['articles']

def process_news_sources(news_source):
    news_list = []
    all_news = get_news_sources(news_source)
    for article in all_news:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urltoImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        news_object = News_Source(author,title,description,url,urltoImage,publishedAt,content)
        news_list.append(news_object)

    return news_list

def get_all_sources():
    url = f'https://newsapi.org/v2/top-headlines/sources?apiKey={api_key}'
    response = requests.get(url)
    news_source_dict = response.json()

    return news_source_dict['sources']

def process_all_sources():
    news_sources_list = []
    all_news = get_all_sources()
    for source in all_news:
        news_id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        news_sources_object = All_news_sources(news_id,name,description,url)
        news_sources_list.append(news_sources_object)

    return news_sources_list