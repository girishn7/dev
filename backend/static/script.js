async function getStockPrice() {
    const symbol = document.getElementById('symbolInput').value;
    const resultDiv = document.getElementById('result');

    if (!symbol) {
        resultDiv.innerHTML = "⚠️ Please enter a stock symbol!";
        return;
    }

    try {
        const response = await fetch(`/api/stock-price?symbol=${symbol}`);
        if (!response.ok) {
            throw new Error("Stock not found or API error");
        }
        const data = await response.json();
        resultDiv.innerHTML = `📈 <strong>${data.symbol}</strong> Price: $${data.price}`;
    } catch (error) {
        resultDiv.innerHTML = `❌ ${error.message}`;
    }
}
