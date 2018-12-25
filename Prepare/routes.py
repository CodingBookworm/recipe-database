import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from Prepare import app, db, bcrypt
#from flaskDemo.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, AssignForm
#from flaskDemo.models import Users, Recipes, Ingredients...
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template('projecthome.html', title='Prepare')

 