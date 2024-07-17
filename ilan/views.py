from flask import Blueprint, render_template, request,flash,redirect,url_for
from .models import Product
from . import db
from flask import render_template, request

views = Blueprint('views', __name__)


@views.route('/')
def home():
    items = Product.query.filter_by()
    return render_template('home.html', items=items)





@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search')
        items = Product.query.filter(Product.product_name.ilike(f'%{search_query}%')).all()
        return render_template('search.html', items=items)

    return render_template('search.html')

@views.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@views.route('/hakkimizda')
def hakkimizda():
    return render_template('hakkimizda.html')

@views.route('/views/<int:id>')

def profile(id):
    ilan = Product.query.get(id)
    return render_template('ilan.html', ilan=ilan)