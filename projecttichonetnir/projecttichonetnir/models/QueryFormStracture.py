
### ----------------------------------------------------------- ###
### --- include all software packages and libraries needed ---- ###
### ----------------------------------------------------------- ###
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField 
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField, DateField,BooleanField
from wtforms import validators, ValidationError

from wtforms.validators import DataRequired
### ----------------------------------------------------------- ###




## This class have the fields that are part of the Country-Capital demonstration
## You can see two fields:
##   the 'name' field - will be used to get the country name
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class QueryFormStructure(FlaskForm):
    name   = StringField('Country Name:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')




## This class have the fields that are part of the Login form.
##   This form will get from the user a 'username' and a 'password' and sent to the server
##   to check if this user is authorised to continue
## You can see three fields:
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class LoginFormStructure(FlaskForm):
    username   = StringField('Username:  ' , [validators.Length(min=2)])
    password   = PasswordField('Password:  ',[validators.Length(min=2)])
    submit = SubmitField('Submit')



## This class have the fields of a registration form
##   This form is where the user can register himself. It will have sll the information
##   we want to save on a user (general information) and the username ans PW the new user want to have
## You can see three fields:
##   the 'FirstName' field - will be used to get the first name of the user
##   the 'LastName' field - will be used to get the last name of the user
##   the 'PhoneNum' field - will be used to get the phone number of the user
##   the 'EmailAddr' field - will be used to get the E-Mail of the user
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ', [validators.Length(min=2)])
    LastName   = StringField('Last name:  ' , [validators.Length(min=2)])
    PhoneNum   = StringField('Phone number:  ' , [validators.Length(min=10,max = 10)])
    EmailAddr  = StringField('E-Mail:  ' , [validators.Email()])
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Password:  ' , [validators.Length(min=2)])



## This class have the fields that the user can set, to have the query parameters for analysing the data
##   This form is where the user can set different parameters, that will be used to do the data analysis (using Pandas etc.)
##  You can see three fields:
##   The fields that will be part of this form are specific to your project
##   Please complete this class according to your needs
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)


class Producer(FlaskForm):
    maxbudget = IntegerField('The Max budget you can invest: ', validators = [DataRequired()])
    minbudget = IntegerField('The Min budget you can invest: ', validators = [DataRequired()])
    genre = SelectField('Your movie genre: ' , validators = [DataRequired] , choices=[('Romance', 'Romance'), ('Comedy', 'Comedy'), ('Crime', 'Crime') , ('War', 'War'), ('Drama', 'Drama'), ('Family', 'Family'), ('Action', 'Action'), ('Animation', 'Animation'), ('Science Fiction', 'Science Fiction'),('Adventure', 'Adventure'),('Horror', 'Horror')])  
    submit = SubmitField('Submit')


