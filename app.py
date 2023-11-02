from flask import Flask, render_template, request
import requests
import json
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    currency_from = request.args.get('formSelectFrom')
    currency_to = request.args.get('formSelectTo')
    input_value = request.args.get('userinput')

    url = f'https://api.exchangerate-api.com/v4/latest/{currency_from}'
    response = requests.get(url)

    data = json.loads(response.text)
    exchange = data["rates"][currency_to]
    result = float(input_value) * float(exchange)

    currency = ['USD','EUR','BRL','JPY','CAD','AUD','CNY']
    simbol = ['$', '€', 'R$', '¥', 'C$', 'A$', 'C¥']

    if currency_to in currency:
        for currency_position in currency:
            currency_position = currency.index(currency_to)
            currency_simbol = simbol[currency_position]

        result_format = f'{currency_simbol} {result:,.2f}'

    return render_template('convert.html', result_format=result_format)

if __name__ == '__main__':
    app.run()