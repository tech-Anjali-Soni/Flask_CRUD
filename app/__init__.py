from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student1.db'
    app.config['SECRET_KEY'] = 'tecdev'
    db.init_app(app)
    Bootstrap(app)
    from .routes import main
    app.register_blueprint(main)
    return app
