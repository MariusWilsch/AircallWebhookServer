from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)


@app.route("/aircall/webhook", methods=["POST"])
def handle_webhook():
    data = request.json
    print(data)  # For demonstration purposes
    # Process the data asynchronously here
    return jsonify(success=True), 200


if __name__ == "__main__":
    app.run(port=500)
