from flask import Flask, jsonify
import json

app = Flask(__name__)

# API route jo data.json ko read karega
@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

get_data()
# Run the Flask app
