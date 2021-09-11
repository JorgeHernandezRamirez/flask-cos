from flask import Flask, jsonify

from cos import cos

app = Flask(__name__)


@app.route("/health")
def health():
    return '200'


@app.route("/bucket")
def buckets():
    return jsonify([bucket['Name'] for bucket in cos.list_buckets()['Buckets']])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
