from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn
import os

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# 1️⃣ API routes first


def get_stock_price(symbol: str):
    api_key = "75a0762ab59743a5a9a0215a6d95495f"
    url = f"https://api.twelvedata.com/price?symbol={symbol}&apikey={api_key}"
    print(f"[DEBUG] Requesting {url}")
    try:
        r = requests.get(url, timeout=10)
        print(f"[DEBUG] Status {r.status_code}, Body {r.text}")
        if r.status_code == 200:
            data = r.json()
            if "price" in data:
                return float(data["price"])
    except Exception as e:
        print(f"[ERROR] {e}")
    return None


@app.get("/api/stock-price")
async def read_stock(symbol: str):
    s = symbol.strip().upper().replace('"', '').replace("'", "")
    price = get_stock_price(s)
    if price is not None:
        return {"symbol": s, "price": price}
    return JSONResponse(status_code=404, content={"error": "Failed to fetch stock price"})

# 2️⃣ Serve static files under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3️⃣ Serve index.html at root


@app.get("/", response_class=FileResponse)
async def index():
    return os.path.join("static", "index.html")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
