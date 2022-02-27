from flask import render_template
from app_news import app
from .request import process_articles, process_categories, process_news_sources
from datetime import datetime

@app.route('/')
@app.route('/home')
def index():
    all_articles = process_articles()
    return render_template('home.html', articles = all_articles, datetime1=datetime)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%B %d, %Y'):
    return value.strptime(format)

@app.route('/categories/<category>')
def categories(category):
    all_categories = process_categories(category)
    return render_template('categories.html', categories=all_categories, name=category)

@app.route('/source/<news_source>')
def news_sources(news_source):
    all_news = process_news_sources(news_source)
    return render_template('news-source.html', news=all_news, name=news_source)