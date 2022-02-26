from turtle import title
from flask import render_template
from app_news import app

@app.route('/')
def index():
    title = 'TheDailyNews by LemmyMwaura'
    return render_template('home.html', title=title)