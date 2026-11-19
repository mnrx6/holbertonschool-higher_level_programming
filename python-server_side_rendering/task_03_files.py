#!/usr/bin/python3
"""Flask application to display products from JSON or CSV."""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    items_list = data.get('items', [])

    return render_template('items.html', items=items_list)


def read_json_products():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_products():
    with open('products.csv', 'r', encoding='utf-8', newline='') as file:
        return list(csv.DictReader(file))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_list = read_json_products()

    elif source == 'csv':
        products_list = read_csv_products()

    else:
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    if product_id is not None:
        products_list = [
            product for product in products_list
            if str(product['id']) == product_id
        ]

        if not products_list:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=products_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
