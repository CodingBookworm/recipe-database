from datetime import datetime
from Prepare import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Recipes(db.Model):
    __table__ = db.Model.metadata.tables['recipes']
    
class Ingredients(db.Model):
    __table__ = db.Model.metadata.tables['ingredients']

class Categories(db.Model):
    __table__ = db.Model.metadata.tables['categories']
    
class IsIn(db.Model):
    __table__ = db.Model.metadata.tables['isin']
class Contains(db.Model):
    __table__ = db.Model.metadata.tables['contains']
class SavedRecipes(db.Model):
    __table__ = db.Model.metadata.tables['savedrecipes']

    

  
