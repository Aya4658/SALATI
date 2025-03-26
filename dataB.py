import requests
from json import *
from flask import Flask,render_template
from datetime import datetime
import time
from plyer import notification

app = Flask(__name__)


@app.route("/")
def index():

  dt = datetime.now().date().strftime("%d-%m-%Y")

  url = f'https://api.aladhan.com/v1/timingsByCity?country=MA&city=Fez&method=21&date={dt}'

  r = requests.get(url)

  

  #print(r.json())

  prayers = r.json()['data']
  DATE = r.json()['data']['date']

  F=r.json()['data']['timings']['Fajr']
  D=r.json()['data']['timings']['Dhuhr']
  A=r.json()['data']['timings']['Asr']
  M=r.json()['data']['timings']['Maghrib']
  I=r.json()['data']['timings']['Isha']

  
  if time.strftime("%H:%M")==F:
    notification.notify(title="صلاة الفجر",message="حان موعد صلاة الفجر",timeout=5)
  if time.strftime("%H:%M")==D:
    notification.notify(title="صلاة الظهر",message="حان موعد صلاة الظهر",timeout=5)
  if time.strftime("%H:%M")==A:
    notification.notify(title="صلاة العصر",message="حان موعد صلاة العصر",timeout=5)
  if time.strftime("%H:%M")==M:
    notification.notify(title="صلاة المغرب",message="حان موعد صلاة المغرب",timeout=5)
  if time.strftime("%H:%M")==I:
    notification.notify(title="صلاة العشاء",message="حان موعد صلاة العشاء",timeout=5)
    

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