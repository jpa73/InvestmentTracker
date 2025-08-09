from flask import Flask, render_template, request, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

# In-memory "database"
investments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_investment', methods=['POST'])
def add_investment():
    data = request.get_json()
    investments.append(data)
    return jsonify({"message": "Investment added successfully"})

@app.route('/get_investments', methods=['GET'])
def get_investments():
    responses = []
    for inv in investments:
        ticker = inv["symbol"]
        start_date = inv["start_date"]
        data = yf.Ticker(ticker)
        historical = data.history(start=start_date, end=start_date)
        if historical.empty:
            return jsonify({"error": f"No data found for start date for {ticker}"}), 404
        
        start_price = historical['Close'].iloc[0]
        current_price = data.history(period="1d")['Close'].iloc[-1]
        pct_change = ((current_price - start_price) / start_price) * 100
        responses.append({
            "symbol": ticker,
            "start_date": start_date,
            "start_price": round(start_price, 2),
            "current_price": round(current_price, 2),
            "pct_change": round(pct_change, 2)
        })
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)
