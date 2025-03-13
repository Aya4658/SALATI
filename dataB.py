import requests
from json import *
from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():

  dt = datetime.now().date().strftime("%d-%m-%Y")

  url = f'https://api.aladhan.com/v1/timingsByCity?country=MA&city=Fez&method=21&date={dt}'

  r = requests.get(url)

  #print(r.json())

  prayers = r.json()['data']
  DATE = r.json()['data']['date']

  #print(prayers)
  
  return render_template("app.html", prayers=prayers, DT=DATE)

if __name__ == "__main__":
    app.run(debug=True)


'''How to run the code on the browser?
  to run the application on the browser:
    1.open terminal
    2.get the python file directory: (like: cd C:/project/folder/)
    3.run the command: python dataB.py 
    4.while clicking on ctrl , click usig mouse on the localhost that appears ( http://127.0.0.1:5000 )
'''