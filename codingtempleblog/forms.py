from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, length
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()]) #Might need to change casing
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = StringField('Content',validators=[DataRequired()])
    submit = SubmitField("Submit")

class PaymentForm(FlaskForm):
    card = StringField('Card Number', validators=[DataRequired()])
    experation = StringField('Experation',validators=[DataRequired()])
    cvv = StringField('CVV',validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit Payment')