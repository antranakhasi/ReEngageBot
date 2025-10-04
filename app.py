from slack import app
from pyngrok import ngrok
import threading

PORT = 3000

def start_ngrok():
    public_url = ngrok.connect(PORT)
    print(f"🌐 Public ngrok URL: {public_url}/slack/events")
    print("Set this as your Slack Request URL in your Slack app.")

if __name__ == "__main__":
    threading.Thread(target=start_ngrok, daemon=True).start()
    app.start(port=PORT)