import json

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {
    "balance": 0,
    "transactions": []
}


@app.route("/")
def get_transactions_history():
    return json.dumps(data)


@app.route("/transaction/add", methods=["POST"])
def add_transaction():
    item = request.get_json()
    data["transactions"].append(item)
    data["balance"] += int(item["amount"])
    return item


if __name__ == "__main_":
    app.run(debug=True, port=5000)
