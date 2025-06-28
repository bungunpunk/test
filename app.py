from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock')
def get_stock():
    symbol = request.args.get('symbol', 'AAPL')
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d')
    return jsonify(data.to_dict())
