async function getStockPrice() {
    const symbol = document.getElementById('symbolInput').value.trim();
    const resultDiv = document.getElementById('result');
    const spinner = document.getElementById('spinner');

    if (!symbol) {
        Swal.fire('⚠️ Oops!', 'Please enter a stock symbol.', 'warning');
        return;
    }

    spinner.classList.remove('hidden');
    resultDiv.innerHTML = "";

    try {
        const response = await fetch(`/api/stock-price?symbol=${symbol}`);
        spinner.classList.add('hidden');

        if (!response.ok) {
            throw new Error("Stock not found or API error");
        }
        const data = await response.json();
        resultDiv.innerHTML = `📈 <strong>${data.symbol}</strong><br>💲Price: $${data.price}`;
        Swal.fire(' Success!', `${data.symbol} Price Loaded`, 'success');
    } catch (error) {
        spinner.classList.add('hidden');
        Swal.fire(' Error!', error.message, 'error');
    }
}
