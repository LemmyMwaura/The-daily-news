from app_news import app
from flask import render_template, request
from .request import process_all_sources

@app.errorhandler(404)
def not_Found(e):
    all_sources = process_all_sources()
    return render_template('404.html', sources=all_sources)