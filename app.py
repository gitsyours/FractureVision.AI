from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    # 🔥 Replace this with your model logic
    text = data.get("text", "")
    
    result = f"Processed: {text}"
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)