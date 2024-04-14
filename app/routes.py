# app/routes.py
from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import PlayerForm, PredictionForm
from app.models import Player
from app.predictor import NBASalaryPredictor
from sqlalchemy.exc import DataError, IntegrityError

# Instantiate your predictor class
salary_predictor = NBASalaryPredictor()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    try:
        if form.validate_on_submit():
            player = Player(
                name=form.name.data, 
                predicted_salary=form.predicted_salary.data, 
                actual_salary=form.actual_salary.data,
                image_url=form.image_url.data
            )
            db.session.add(player)
            db.session.commit()
            flash('Player added successfully!')
            return redirect(url_for('index'))
    except (DataError, IntegrityError) as e:
        db.session.rollback()
        flash('An error occurred. Please try again.')
        print(f"Error adding player: {e}")
    except Exception as e:
        db.session.rollback()
        flash('A server error occurred.')
        print(f"Unexpected error: {e}")
    return render_template('add_player.html', form=form)

@app.route('/predict_salary', methods=['GET', 'POST'])
def predict_salary():
    form = PredictionForm()
    predicted_salary = None  # Initialize to None
    if form.validate_on_submit():
        # Call the prediction method
        raw_salary = salary_predictor.predict_salary(
            form.points_per_game.data,
            form.rebounds_per_game.data,
            form.assists_per_game.data
        )
        # Format the predicted salary here
        predicted_salary = f"${raw_salary:,.2f}"
        return render_template('predict_result.html', predicted_salary=predicted_salary)
    return render_template('predict_salary.html', form=form)


@app.route('/get_player/<name>')
def get_player(name):
    player = Player.query.filter_by(name=name).first()
    if player:
        return jsonify(player.to_dict())
    else:
        return jsonify({'error': 'Player not found'}), 404
