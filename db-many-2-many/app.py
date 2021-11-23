from flask import Flask
from flask_sqlalchemy import SQLALchemy
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLALchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    enrolments = db.relationship('Enrolments', backref='students')

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(30), nullable=False)
    enrolments = db.relationship('Enrolments', backref='class')

class Enrolments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    class_id = db.Column('classes_id', db.Integer, db.ForeignKey('classes.id'))
    student_id = db.Column('student_id', db.Integer, db.ForeignKey('students.id'))
    enrollment_date = db.Column('Date', db.String(30))

if __name__ == '__main__':
    app.run(debug==True, host = '0.0.0.0')
    
