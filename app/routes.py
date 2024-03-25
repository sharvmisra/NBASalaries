# app/routes.py
from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import PlayerForm
from app.models import Player

@app.route('/', methods=['GET', 'POST'])
def index():
    # The form is not actually used on this route in this code
    return render_template('index.html')

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    if form.validate_on_submit():
        print("Form data:", form.data)  # Print form data to the console
        player = Player(
            name=form.name.data, 
            predicted_salary=form.predicted_salary.data, 
            actual_salary=form.actual_salary.data,
            image_url=form.image_url.data
        )
        db.session.add(player)
        db.session.flush()  # This will allow you to check data before committing
        print("New player object:", player)  # Print new player object to the console
        print("New player image URL:", player.image_url)  # Specifically print the image URL
        db.session.commit()
        flash('Player added successfully!')
        return redirect(url_for('index'))
    return render_template('add_player.html', form=form)


@app.route('/get_player/<name>')
def get_player(name):
    player = Player.query.filter_by(name=name).first()
    if player:
        return jsonify(player.to_dict())
    else:
        return jsonify({'error': 'Player not found'}), 404
