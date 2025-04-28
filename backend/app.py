from fastapi import FastAPI
import requests

app = FastAPI()


def get_stock_price(symbol: str):
    api_key = "f10a86ac03294d758aa1eb2b027b13f4"  # Replace with your key
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "price" in data:
            return float(data["price"])
        else:
            return None
    else:
        return None


@app.get("/stock/{symbol}")
async def read_stock(symbol: str):
    symbol = symbol.replace('"', '').replace("'", "").upper()
    price = get_stock_price(symbol)
    if price:
        return {"symbol": symbol, "price": price}
    else:
        return {"error": "Failed to fetch stock price"}
