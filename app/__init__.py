# third party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

# initialising the flask-login loginManager object
login_manager = LoginManager()


# the following method accepts environment variable as its variable
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # initializing the login manager class
    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page.'
    login_manager.login_view = 'auth.login'

    # initializing migrations
    migrate = Migrate(app, db)

    # initialising bootstrap
    Bootstrap(app)

    from app import models

    # the added url prefix, /admin means that the views for this blueprint
    # will be accessed in the browser with the url prefix 'admin'
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # GENERATING CUSTOM ERROR PAGES

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='forbidden'),403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='page not found'),404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='server error'),500

    return app













