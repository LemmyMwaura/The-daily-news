from flask import render_template
from app_news import app
from .request import process_all_sources, process_articles, process_categories, process_news_sources
from datetime import datetime

@app.route('/')
@app.route('/home')
def index():
    all_articles = process_articles()
    all_sources = process_all_sources()
    return render_template('home.html', articles = all_articles, sources = all_sources, datetime1=datetime)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y'):
    return value.strptime(format)

@app.route('/categories/<category>')
def categories(category):
    all_categories = process_categories(category)
    all_sources = process_all_sources()
    return render_template('categories.html', sources = all_sources, categories=all_categories, name=category)

@app.route('/sources/<news_source>')
def news_sources(news_source):
    all_news = process_news_sources(news_source)
    all_sources = process_all_sources()
    return render_template('news-source.html',  sources = all_sources, news=all_news, name=news_source)