from flask import Flask, Response, request, render_template
import json
import MySQLdb

from model import connect_to_db, db, KilnData

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/temperature", methods=['GET'])
def temperature():
  data = db.session.query(KilnData).all()
  jsonData = json.dumps([r.to_dict() for r in data], default=str)
  resp = Response(jsonData, status=200, mimetype='application/json')
  return resp

if __name__ == "__main__":
  connect_to_db(app)
  app.run()
