from flask import Flask
from flask_sqlalchemy import SQLALchemy
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLALchemy(app)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order = db.Column(db.Integer, unique = True)
    product = db.relationship('Products', backref='orders')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable= False)
    order = db.relationship('Orders', backref='products')

class Product_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))    
    product_id = db.Column('products_id', db.Integer, db.ForeignKey('products.id'))
    product2order = db.Column('product2order', db.String(30))

if __name__ == '__main__':
    app.run(debug==True, host = '0.0.0.0')



