from flask import render_template

from app.blueprints.news.controller import news
from .models.article import Article
from ..auth.models.role import Permission


@news.route('/', methods=['GET', 'POST'])
def home():
    articles = Article.query.all()
    return render_template('news.html', articles=articles)


@news.route('/add_news')
def add_news():
    return 'add news'


@news.route('/delete_news')
def delete_news():
    return 'delete news'


@news.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
