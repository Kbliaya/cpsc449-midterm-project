from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

conn = pymysql.connect(
    host='localhost',
    user='root',
    password = "1234567890",
    db='449MidtermProject_db',
    cursorclass=pymysql.cursors.DictCursor
)
cur = conn.cursor()

@app.route("/")
def home():
    return "Hello"

@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

@app.errorhandler(401)
def unauthenticated(e):
    return jsonify(error=str(e)), 401

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))