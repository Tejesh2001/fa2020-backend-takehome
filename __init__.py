from flask import Flask, redirect
import csv 
import json

import random

app = Flask(__name__)


"""

TASK

Implement an endpoint `/api/fetch` that returns the contents of `data.csv` as JSON

1) Load/transcribe `data.csv`
2) Save each entry's full name, time zone, and department
3) Return the JSON data at the endpoint

"""
##Part 1
data = {} 
#List to store all employees
employees = [] 
csvFilePath = "data.csv"
try:
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)            
    
        for rows in csvReader: 
                
            # Each rows is a dict for each row in the excel sheet with the first entry in the each column as it's key
            key = rows['id']
            dict_copy = {}
            #Making another dict to store each employee
            dict_copy['name'] = rows['first_name'] + " " + rows["last_name"]
            dict_copy['timezone'] = rows['time_zone']
            dict_copy['dept'] = rows['dept']
            employees.append(dict_copy)
except:
    print(Exception("Invalid file/Invalid file path"))
    exit()
    

data['employees'] = employees
#Converting to json and saving in another file
#Part 2
with open("csv_to_json.json", 'w', encoding='utf-8') as jsonf: 
    jsonf.write(json.dumps(data, indent=4))
json_string = json.dumps(data, indent=4)


"""

DOCUMENTATION WEBPAGE BELOW

"""
#Part 3
@app.route("/api/fetch")
def csv_data():
    return """
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }

            pre, code {
                background: #121212;
                color: white;
            }

            code {
                padding: 4px;
            }

            pre code {
                padding: 0;
            }

            pre {
                padding: 10px;
            }

            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>""" + json_string + """
        <br />]</code></pre>"""


@app.route("/")
def redirect_to_api():
    return redirect("/api", code=301)

@app.route("/api")
def api_home():
    return """
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }

            pre, code {
                background: #121212;
                color: white;
            }

            code {
                padding: 4px;
            }

            pre code {
                padding: 0;
            }

            pre {
                padding: 10px;
            }

            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>employees: [
            <br />  {
            <br />      name: <i>FULL NAME OF EMPLOYEE</i>,
            <br />      timezone: <i>TIMEZONE</i>,
            <br />      dept: <i>EMPLOYEE'S DEPARTMENT</i>,
            <br />  }
            <br />  ...
        <br />]</code></pre>"""
