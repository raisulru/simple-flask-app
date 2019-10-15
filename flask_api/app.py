import click
from flask import Flask, redirect, url_for
from .config import *
# from .Controllers import Apiv1Routes, ErrorRoutes
from .Models import User, Database 

# App init
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Database and Marshmallow init to avoid cycling import
Database.db.init_app(app)
Database.ma.init_app(app)

# Blueprint register
# app.register_blueprint(Apiv1Routes.bp, url_prefix='/api/v1')
# app.register_blueprint(ErrorRoutes.bp)

# This can be deleted!
@app.route("/")
def _redirect():
    return redirect(url_for('api_v1.root'))

# CLI
@app.cli.command()
def init_db(): 
    click.echo('Dropping tables')
    Database.db.drop_all()
    click.echo('Creating tables')
    Database.db.create_all()
    Database.db.session.commit()

