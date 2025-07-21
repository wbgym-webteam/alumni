from flask import Flask, render_template, redirect
import sqlalchemy
from flask_sqlalchemy import *
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import path as Path
import secrets


env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv()


def create_app():
    app = Flask(__name__)
    db = sqlalchemy.SQLAlchemy(app)


    # Create and configure the app with explicit instance path
    src_dir = Path(__file__).parent.parent.absolute()
    instance_dir = os.path.join(src_dir, 'instance')
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or secrets.token_hex(32)




    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_dir, "wbgym.db")}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =

    db.init_app(app)
    migrate = Migrate(app, db)


    with app.app_context():
        
        import user_views
        import admin_views


        app.register_blueprint(user_views.user_bp, url_prefix="/")
        app.register_blueprint(admin_views.admin_bp, url_prefix="/")

        # db.drop_all()
        db.create_all()

        return app