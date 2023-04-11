# CPSC 449-02 Midterm Project
## Team Members:
* Kaylee Bliaya
* Alan Blandon
* Andrew Lau

## Setup:
1. Create new database that contains a table with the following schema:
'''
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3
'''

2. Create a virtual environment and install the following packages:
    * flask
    * pymysql
    * flask_cors
    * werkzeug.utils
    * os
    * re
3. Run the flask application with the command "flask run"
    * If you're using windows use the command "python -m flask run"

4. In Postman create and send the following requests:
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
    * value = file to be uploaded