from flask import Flask, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import mysql.connector
import json
from utils.parser import Company

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'jobTicker'

mysql = MySQL(app)

@app.route('/', methods = ['GET'])
def getCompanies():
    cursor = mysql.connection.cursor()
    cursor.execute(""" SELECT DISTINCT * FROM companies NATURAL JOIN
                   company_positions; """)
    data = cursor.fetchall()
    cursor.close()
    res = {"body": [x for x in data]}

    return json.dumps(res)

@app.route('/location', methods = ['GET'])
def getCompanyLocations():
    args = request.args
    company_name = args.get("company")

    cursor = mysql.connection.cursor()
    cursor.execute(""" SELECT location FROM company_locations WHERE
                   LOWER(company_name) = LOWER(%s)""", [company_name])

    data = cursor.fetchall()
    cursor.close()
    res = {"body": [x for x in data]}

    return json.dumps(res)

app.run(host='0.0.0.0', port=8080)
