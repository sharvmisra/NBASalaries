# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, Optional, URL

class PlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired(), Length(max=50)])
    predicted_salary = StringField('Predicted Salary', validators=[DataRequired(), Length(max=20)])
    actual_salary = StringField('Actual Salary', validators=[DataRequired(), Length(max=20)])
    image_url = StringField('Player Image URL', validators=[Optional(), URL(), Length(max=255)])
    submit = SubmitField('Add Player')

class PredictionForm(FlaskForm):
    points_per_game = FloatField('Points Per Game', validators=[DataRequired()])
    assists_per_game = FloatField('Assists Per Game', validators=[DataRequired()])
    rebounds_per_game = FloatField('Rebounds Per Game', validators=[DataRequired()])
    submit = SubmitField('Predict Salary')

# The existing PlayerForm remains unchanged
