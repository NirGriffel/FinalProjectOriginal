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

import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError

from projecttichonetnir.models.QueryFormStracture import QueryFormStructure 
from projecttichonetnir.models.QueryFormStracture import LoginFormStructure
from projecttichonetnir.models.QueryFormStracture import UserRegistrationFormStructure
from projecttichonetnir.models.QueryFormStracture import Producer

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

db_Functions = create_LocalDatabaseServiceRoutines() 

#--------------------------------------------------------------------------------
# no page - 
#This page connects between the Login page to the Register page to one page that give the user option to choose if he want to login or regist.
# He has no reference in layout
#--------------------------------------------------------------------------------
@app.route('/')
@app.route('/no')
def no():
    print("no")
    return render_template(
        'no.html',
        title='Home Page',
        year=datetime.now().year,
    )

#--------------------------------------------------------------------------------
# home page - 
#This page give informtion about the project - what is my field of research
#--------------------------------------------------------------------------------
@app.route('/home')
def home():
    print("Home")
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


#--------------------------------------------------------------------------------
#contact page -
#This page give informtion about Shows the contact details with me (Gmail, phone)
#--------------------------------------------------------------------------------
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

#--------------------------------------------------------------------------------
#about page -
#This page give informtion about the project What the project is about.
#--------------------------------------------------------------------------------
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

#--------------------------------------------------------------------------------
#data page -
#This page show 2 links to my DataBase.
#--------------------------------------------------------------------------------
@app.route('/data')
def data():
    """Renders the about page."""
    return render_template(
        'data.html',
        title='Data',
        year=datetime.now().year,
        message='Your application description page.'
    )


#--------------------------------------------------------------------------------
#register page -
#the user must have account to start browes in my account, this oage give im the option to registr.
#--------------------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    #התנאי הבוליאני בודק את פרטי המשתמש ברגע שלחץ על כפתור השליחה. 
    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""
            return redirect('Login')
    #אם משהו מפרטיו היו שגואים המשתמש יקבל הודעת שגיאה חזרה למסך 
        else:
            flash('Error: User with this Username already exist !')
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='',
        year=datetime.now().year,
        repository_name='Pandas',
        )


#--------------------------------------------------------------------------------
#login page -
#if the user have allredy account he can login to the site and start browes, this page check if he rellay have account.
#--------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():

    form = LoginFormStructure(request.form)
  #התנאי הבואלי הזה מאמת את פירטי המשתמש מקובץ האקסל שאליו שמורת כל הפרטים.
    # אם קיים משתמש כזה בקובץ היא מאפשר לו להתחבר ואם לא היא מקפיצה לו הודעת שגיאה
    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            return redirect('home')

        else:
            flash('Wrong password and\or username')
   
    return render_template(
        'login.html', 
        form=form, 
        title='',
        year=datetime.now().year,
        repository_name='Pandas',
        )

#--------------------------------------------------------------------------------
#dataSet1 page -
#This page give information about the first database and give the user information to see the dataBase.
#--------------------------------------------------------------------------------
@app.route('/dataSet1')
def dataSet1():
    #הפעולה הזאת קוראת את קובץ הדאטה ובעזרת אנחנו יכולים להציג למשתמש את הקובץ לאחר מכן
    df = pd.read_csv(path.join(path.dirname(__file__),'static\\data\\movieNameandbudget.csv'))
    return render_template(
        'dataSet1.html',
        title='dataSet1',
        year=datetime.now().year,
        message='My Data Set 1', data = df.to_html(classes = "table table-hover")
    )

#--------------------------------------------------------------------------------
#dataSet2 page -
#This page give information about the secound database and give the user information to see the dataBase.
#--------------------------------------------------------------------------------
@app.route('/dataSet2')
def dataSet2():
    #הפעולה הזאת קוראת את קובץ הדאטה ובעזרת אנחנו יכולים להציג למשתמש את הקובץ לאחר מכן
    df2 = pd.read_csv(path.join(path.dirname(__file__),'static\\data\\movienameandincome.csv'))
    return render_template(
        'dataSet2.html',
        title='dataSet2',
        year=datetime.now().year,
        message='My Data Set 2', data = df2.to_html(classes = "table table-hover")
    )

#--------------------------------------------------------------------------------
#query page -
#This page give information about the first database and give the user information to see the dataBase.
#--------------------------------------------------------------------------------
@app.route('/query', methods=['GET', 'POST'])
def query():

    form = Producer()

    #הפעולה קוראת את שתי ממאגרי הנתונים תאפשר לנו עוד מעט בעזרת הגופיטר להציג למשתמש גרף 
    dfbudget = pd.read_csv(path.join(path.dirname(__file__), 'static/data/movieNameandbudget.csv'))
    dfincome = pd.read_csv(path.join(path.dirname(__file__), 'static/data/movienameandincome.csv'))
    #מכיוון שהוויזואל סטודיו לא יודע להציג את הגרף כגרף אנחנו צריכים להעביר אותו לתמונה.
    # אנחנו מגדירים את זה בהתחלה 'ריק' כדי שבשל מאוחר יותר נוכל להכניס את הגרף לתוכו ולהציג אותו למשתמש. 
    chart = ''

    #ברגע שהמשתמש לוחץ אישור לאחר שהזין את הפרטים  מתחיל עריכה של קובץ האקסל לפי הנתונים שהמשתמש ביקש ולאחר מכן הנתונים מוצג בגרף   
    if request.method == 'POST':
        #השלוש שורות הראשונות לוקחות את הנתונים שהמשתמש ומאפשרות לנו לערוך את קובץ הדטא באתם לבקשתו
        gener = form.genre.data
        minbudget = form.minbudget.data
        maxbudget = form.maxbudget.data
        dfbudget = dfbudget.set_index('genre')
        dfbudget = dfbudget.loc[[gener]]
        dfbudget = dfbudget.drop(['mpaa_rating','release_date','rating_count','runtime','movieid','rating'], 1)
        #הפעולה ממינת את קובץ הדטא על פי הטווחים שהמשתמש הזין ותציג לו תוכן בהתאם
        dfbudget = dfbudget.loc[dfbudget['budget'] >= minbudget]
        dfbudget = dfbudget.loc[dfbudget['budget'] <= maxbudget]
        dfbudget = dfbudget.reset_index()
        dfincome = dfincome.set_index('genre')
        dfincome = dfincome.loc[[gener]]
        dfincome = dfincome.drop(['mpaa_rating','release_date','rating_count','runtime','movieid','rating'], 1)
        dfincome = dfincome.rename(columns={'gross': 'income'})
        dfincome = dfincome.reset_index()
        df3 = pd.merge(dfincome,dfbudget)
        df3 = df3.nlargest(20,'budget')
        df3 = df3.set_index('title')
        fig = plt.figure()
        ax = fig.add_subplot(111)
        #יוצר את הגרף על פי הנתונים שהמשתמש הזין. הגרף יהיה בצורה של גרף עמודות
        df3.plot(ax = ax , kind = 'bar', figsize = (24, 15) , fontsize = 18 , grid = True , color=['black','brown'])
        #בשורה הזאת הגרף הופך לתמונה על יידי פונקציה שמוגדרת למטה בשם 
        plot_to_image
        chart = plot_to_img(fig)



    return render_template(
        'query.html', 
        form=form, 
        title='',
        year=datetime.now().year,
        repository_name='Pandas',
        chart = chart
        )

#הפעולה הופכת את הגרף לתמונה בדף ה
#Query
def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String
