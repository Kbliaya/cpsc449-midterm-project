from flask import Flask, request, jsonify, abort, session
import pymysql
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os, re, jwt, datetime
from functools import wraps

# Flask application set up
app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SECRET_KEY'] = 'secretKey'

# connect to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password = '1234567890',
    db='449midtermproject_db',
    cursorclass=pymysql.cursors.DictCursor
)
cur = conn.cursor()

# 400 error handler
@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400

# 401 error handler
@app.errorhandler(401)
def unauthenticated(e):
    return jsonify(error=str(e)), 401

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e)), 500

# route and function for homepage
@app.route('/')
def home():
    return "Hello"

def check_authorization(f):
     @wraps(f)
     def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
             return "You need a token to access this route."
        
        try:
             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
             return "The given token is invalid. You are not authorized to access this route"

        return f(*args, **kwargs)
     return decorated

@app.route('/public_route')
def public_route():
      return "You are in the Public Route! You can now start uploading files!"

@app.route('/protected_route')
@check_authorization
def protected_route():
     return "You are in the Protected Route!"

# route and function to register an account
@app.route('/register', methods =['GET', 'POST'])
def register():
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		
		cur.execute('SELECT * FROM users WHERE username = % s', (username))
		user = cur.fetchone()
		conn.commit()
		
		if user:
			return 'User already exists!'
		elif not re.match(r'[A-Za-z0-9]+', username):
			return 'Name must contain only characters and numbers!'
		else:
			cur.execute('INSERT INTO users VALUES (NULL, % s, % s)', (username, password))
			conn.commit()
		
	elif request.method == 'POST':
		return 'Please fill out the form!'
	return "Account Successfully Registered!"

# route and function to login to an account
@app.route('/login', methods =['GET', 'POST'])
def login():
     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cur.execute('SELECT * FROM users WHERE username = % s AND password = % s', (username, password))
        conn.commit()
        user = cur.fetchone()

        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['username'] = user['username']
            session['password'] = user['password']

            if session['username'] == 'admin' and session['password'] == 'adminPassword':
                token = jwt.encode({'username' : session['username'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])
                return f'{username} Successfully Logged in!\ntoken: {token}'
            return f'{username} Successfully Logged in!'
        else:
            return 'Incorrect username / password!'

# file upload configurations
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

# route and function to upload files
@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'loggedin' in session:
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != "":
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            return "File Successfully Uploaded!"
    else:
        return "Please log in!"

if __name__ == '__main__':
    app.run(host ='localhost', port = int('5000'))