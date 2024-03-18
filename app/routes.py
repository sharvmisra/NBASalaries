# app/routes.py
from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import PlayerForm
from app.models import Player

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(name=form.name.data, predicted_salary=form.predicted_salary.data, actual_salary=form.actual_salary.data)
        db.session.add(player)
        db.session.commit()
        flash('Player added successfully!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(name=form.name.data, predicted_salary=form.predicted_salary.data, actual_salary=form.actual_salary.data)
        db.session.add(player)
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
