import threading
import webview
from app import app

def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()
    webview.create_window("Investment Tracker", "http://127.0.0.1:5000", width=800, height=600)
    webview.start()
