document.getElementById("investmentForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const symbol = document.getElementById("symbol").value;
    const start_date = document.getElementById("start_date").value;

    fetch("/add_investment", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symbol, start_date })
    })
    .then(res => res.json())
    .then(data => {
        alert("Investment Added!");
    });
});

function loadInvestments() {
    fetch("/get_investments")
    .then(res => res.json())
    .then(data => {
        const resultDiv = document.getElementById("result");
        resultDiv.innerHTML = '<h3>Investments:</h3>';
        data.forEach(inv => {
            if (inv.error) {
                resultDiv.innerHTML += `<p style="color: red;">Error for ${inv.symbol}: ${inv.error}</p>`;
            } else {
                resultDiv.innerHTML += `
                    <p>
                        <strong>${inv.symbol}</strong><br>
                        Start Date: ${inv.start_date}<br>
                        Start Price: $${inv.start_price}<br>
                        Current Price: $${inv.current_price}<br>
                        Percentage Change: ${inv.pct_change}%
                    </p>
                    <hr>
                `;
            }
        });
    });
}
