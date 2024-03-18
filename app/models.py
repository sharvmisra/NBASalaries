# app/models.py
from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    predicted_salary = db.Column(db.String(50))
    actual_salary = db.Column(db.String(50))
    image_url = db.Column(db.String(200), default='default_player_image.jpg')

    def __repr__(self):
        return f'<Player {self.name}>'
    
    def to_dict(self):
        return {
            'name': self.name,
            'predicted_salary': self.predicted_salary,
            'actual_salary': self.actual_salary,
            'image_url': self.image_url
        }
