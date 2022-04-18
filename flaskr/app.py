import sys
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.home import menu
from routes.articles import news
from auth import bp

# recogemos los parametros de conexion de la base de datos
load_dotenv(find_dotenv())

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping({
    'ENV': 'development',
    'DEBUG': True,
    'TESTING': False,
    'SECRET_KEY': 'secretkey',
})

SQLAlchemy(app)

app.register_blueprint(bp)
app.register_blueprint(menu)
app.register_blueprint(news)

