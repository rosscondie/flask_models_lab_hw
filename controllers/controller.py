from app import app
from flask import render_template
from models.order_list import order_list

@app.route('/orders')
def index_orders():
    return render_template("index.html", order_list = order_list)

@app.route('/orders/<number>')
def order(number):
    return render_template("order.html", order = order_list[int(number)])