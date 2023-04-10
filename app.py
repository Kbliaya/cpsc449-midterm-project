from flask import Flask, request, jsonify, abort
import pymysql
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

# conn = pymysql.connect(
#     host='localhost',
#     user='root',
#     password = 'insert_password',
#     db='insert_db_name',
#     cursorclass=pymysql.cursors.DictCursor
# )
# cur = conn.cursor()

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

@app.route('/')
def home():
    return "Hello"

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return "File Successfully Uploaded!"

if __name__ == '__main__':
    app.run(host ='localhost', port = int('5000'))