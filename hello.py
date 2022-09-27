from wsgiref.validate import validator
from flask import Flask, render_template, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime as dt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY']='testtesttest'
bootstrap=Bootstrap(app)
moment=Moment(app)

class NameAndEmailForms(FlaskForm):
    name=StringField('What is your name?', validators=[DataRequired()])
    email=EmailField("What is your UofT Email address?", validators=[Email(allow_empty_local=True)])
    submit=SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    substring='utoronto'
    
    nameAndEmailForm=NameAndEmailForms()
    
    if nameAndEmailForm.validate_on_submit():
        oldName=session.get('name')
        oldEmail=session.get('email')
        oldIsValidEmail=session.get('isValidEmail')

        if oldName is not None and oldName !=nameAndEmailForm.name.data: 
            flash('Looks like you have changed your name!')
        if oldEmail is not None and oldEmail !=nameAndEmailForm.email.data: 
            flash('Looks like you have changed your email!')

        session['name']=nameAndEmailForm.name.data
        session['email']=nameAndEmailForm.email.data
        session['isValidEmail']=substring in nameAndEmailForm.email.data

        nameAndEmailForm.name.data=''
        nameAndEmailForm.email.data=''

        return redirect(url_for('index'))
    return render_template('index.html', current_time=dt.utcnow(), form=nameAndEmailForm, name=session.get('name'), email=session.get('email'), isValidEmail=session.get('isValidEmail'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
