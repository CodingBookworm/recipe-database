import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from prepare import app, db, bcrypt
#from flaskDemo.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, AssignForm
from prepare.models import Users, Recipes, Ingredients
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime



@app.route("/")
@app.route("/home")
def home():
    rec = Recipes.query.all()
    for i in rec:
        print(i)
    return render_template('project_home.html', title='Prepare', joined_m_n=rec)

 