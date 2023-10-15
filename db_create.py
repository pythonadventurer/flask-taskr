
from views import db, app
from models import *
from datetime import date


def db_create():
    # create the database and the db table
    with app.app_context():
        db.create_all()
        db.session.commit()
