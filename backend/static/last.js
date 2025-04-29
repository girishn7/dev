function goBack() {
    window.location.href = '/';
  }
  
  window.addEventListener('DOMContentLoaded', () => {
    const last = localStorage.getItem('lastStock');
    const div = document.getElementById('lastData');
    if (last) {
      const data = JSON.parse(last);
      div.innerHTML = `
        <p>📈 <strong>${data.symbol}</strong></p>
        <p>💲 Price: $${data.price}</p>
        <p><em>Fetched at ${new Date().toLocaleTimeString()}</em></p>
      `;
    } else {
      div.textContent = 'No data stored yet. Go fetch a price first!';
    }
  });
  