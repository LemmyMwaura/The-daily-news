from flask import render_template
from app_news import app
from .request import process_articles

@app.route('/home')
@app.route('/')
def index():
    all_articles = process_articles()
    return render_template('home.html', articles = all_articles)