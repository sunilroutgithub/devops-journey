from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask app is running!"})

@app.route("/data")
def data():
    return jsonify({"items": [[1, "DevOps"], [2, "Docker"], [3, "Python"], [4, "CI/CD"]]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Version v2 - Rolling Update
