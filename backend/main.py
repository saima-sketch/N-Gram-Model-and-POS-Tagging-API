
from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp import perform_pos_tagging

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "NLP Practical API is running"
    })


@app.route("/pos-tag", methods=["POST"])
def pos_tag():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter a sentence."}), 400

    try:
        result = perform_pos_tagging(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
