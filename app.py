from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_stock():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'}), 400
    
    stock = yf.Ticker(symbol)
    info = stock.info

    result = {
        'symbol': symbol,
        'shortName': info.get('shortName'),
        'currentPrice': info.get('currentPrice'),
        'marketCap': info.get('marketCap'),
        'currency': info.get('currency'),
        'previousClose': info.get('previousClose')
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

