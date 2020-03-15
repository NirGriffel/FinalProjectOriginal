"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from projecttichonetnir import app
from projecttichonetnir.models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

import pandas as pd


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from projecttichonetnir.models.QueryFormStracture import QueryFormStructure 
from projecttichonetnir.models.QueryFormStracture import LoginFormStructure
from projecttichonetnir.models.QueryFormStracture import UserRegistrationFormStructure 

db_Functions = create_LocalDatabaseServiceRoutines() 



@app.route('/')
@app.route('/home')
def home():
    print("Home")
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/project_resources')
def project_resources():

    print("Project Resources")

    """Renders the about page."""
    return render_template(
        'project_resources.html'
    )


@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Your application description page.'
    )



@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )

df = pd.read_csv("C:\\Users\\Nir\\source\\repos\\projecttichonetnir\\projecttichonetnir\\projecttichonetnir\\static\\data\\movieNameandbudgetב.csv")
@app.route('/dataSet1')
def dataSet1():
    """Renders the about page."""
    return render_template(
        'dataSet1.html',
        title='dataSet1',
        year=datetime.now().year,
        message='My Data Set 1', data = df.to_html(classes = "table table-hover")
    )

df2 = pd.read_csv("C:\\Users\\Nir\\source\\repos\\projecttichonetnir\\projecttichonetnir\\projecttichonetnir\\static\\data\\movienameandincome.csv")
@app.route('/dataSet2')
def dataSet2():
    """Renders the about page."""
    return render_template(
        'dataSet2.html',
        title='dataSet2',
        year=datetime.now().year,
        message='My Data Set 2', data = df2.to_html(classes = "table table-hover")
    )











