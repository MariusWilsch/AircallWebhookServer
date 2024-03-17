from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1 style='text-align: center;'>Aircall Webhook Server is Running</h1>"

@app.route("/aircall/webhook", methods=["POST"])
def handle_webhook():
  # Handle the webhook payload from Aircall
  data = request.json
  print(data)  # For demonstration, print the data to console

  # Process the data asynchronously here (e.g., queue a background job)

  # Always return a 200 HTTP status code to Aircall
  return jsonify(success=True), 200

if __name__ == "__main__":
  app.run(port=5000)
