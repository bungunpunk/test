from fastapi import FastAPI, Query
import yfinance as yf

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "欢迎使用 yfinance API！"}

@app.get("/stock")
def get_stock_data(ticker: str = Query(..., description="股票代号，比如 AAPL")):
    try:
        stock = yf.Ticker(ticker)
        return {
            "symbol": stock.info.get("symbol"),
            "longName": stock.info.get("longName"),
            "price": stock.info.get("currentPrice"),
            "currency": stock.info.get("currency"),
            "marketCap": stock.info.get("marketCap"),
            "sector": stock.info.get("sector")
        }
    except Exception as e:
        return {"error": str(e)}
