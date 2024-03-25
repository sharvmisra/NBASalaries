# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Optional, URL

class PlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    predicted_salary = StringField('Predicted Salary', validators=[DataRequired()])
    actual_salary = StringField('Actual Salary', validators=[DataRequired()])
    image_url = StringField('Player Image URL', validators=[Optional(), URL()])
    submit = SubmitField('Add Player')
