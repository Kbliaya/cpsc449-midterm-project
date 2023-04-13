# CPSC 449-02 Midterm Project
## Team Members:
* Kaylee Bliaya
* Alan Blandon
* Andrew Lau

## Setup:
1. Create new database that contains a table with the following schema:
```
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3
```

2. Replace lines 18 and 19 in app.py with the database password and name you created in step 1.
```
conn = pymysql.connect(
    host='localhost',
    user='root',
    password = 'insert_password',   <------- replace with database password
    db='insert_db_name',   <------- replace with database name
    cursorclass=pymysql.cursors.DictCursor
)
```

3. Create a virtual environment and install the following packages:
    * cryptography==40.0.1
    * Flask==2.2.3
    * Flask-Cors==3.0.10
    * mysqlclient==2.1.1
    * PyJWT==2.6.0
    * PyMySQL==1.0.3
    * Werkzeug==2.2.3
4. Run the flask application with the command "flask run"
    * If you're using windows use the command "python -m flask run"

5. In Postman create and send the following requests:
    * Register
        * POST [url from flask run]/register
        * Navigate to Body -> form-data
            * row 1 key = username
            * row 1 value = any username
            * row 2 key = password
            * row 2 value = any password
    * Login
        * POST [url from flask run]/login
        * Navigate to Body -> form-data
            * row 1 key = username
            * row 1 value = any username
            * row 2 key = password
            * row 2 value = any password
    * Access Public Route
        * GET [url from flask run]/public_route
    * Access Protected Route
        * GET [url from flask run]/protected_route
        * In Query Params enter:
            * key = token
            * Value = token from login
    * File Upload
        * POST [url from flask run]/file_upload
        * Navigate to Body -> form-data
        * select file from the dropdown in the Key column
        * key = file
        * value = file to be uploaded (select a file to upload)

## POSTMAN Endpoints
![CPSC449 - Midterm Project Endpoints](https://user-images.githubusercontent.com/54484110/231060939-678daa98-6141-4fcd-9267-7fac70f2a967.png)
