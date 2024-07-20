# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DecimalField, FileField
from wtforms.validators import DataRequired

class CarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    description = TextAreaField('Description')
    image = FileField('Image', validators=[DataRequired()])
