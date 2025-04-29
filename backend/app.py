from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

# Serve static frontend
app.mount("/", StaticFiles(directory="static", html=True), name="static")


def get_stock_price(symbol: str):
    api_key = "951deeca533749fab80f572a022b5796"  # Your Twelve Data API key
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


# API endpoint for frontend
@app.get("/api/stock-price")
async def read_stock(symbol: str):
    symbol = symbol.replace('"', '').replace("'", "").upper()
    price = get_stock_price(symbol)
    if price:
        return {"symbol": symbol, "price": price}
    else:
        return JSONResponse(status_code=404, content={"error": "Failed to fetch stock price"})


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
