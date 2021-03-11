import logging
from postgresql_person import PostgreSQL
from flask import Flask, render_template, request

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

db = PostgreSQL()
db.connect()

if db.isconnected:
    if db.create_table():
        if db.empty():
            db.insert_id(0)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return render_template("index.html")

@app.route("/inc/", methods=['GET'])
def increment():
    if db.isconnected and db.increment_id():
        return "increment id"

@app.route("/id/", methods=['GET'])
def current():
    if db.isconnected and db.get_id():
        return "curent id : " + str(db.id)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)