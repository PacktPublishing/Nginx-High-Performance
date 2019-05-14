from flask import Flask
from flask import render_template
from flask import request
import datetime
import memcache
import cgi

app = Flask(__name__)
cache = memcache.Client(["127.0.0.1:11211"])

class AppdateTime :
    def __init__(self, day, date, time):
        self.day = day
        self.date = date
        self.time = time


@app.route("/")
def hello():
    d = datetime.datetime.now();
    today = AppdateTime(d.strftime("%A"),d.strftime("%d %B"), d.strftime("%H:%M:%S %p"))
    d = d + datetime.timedelta(days=1)
    tom = AppdateTime(d.strftime("%A"),d.strftime("%d %B"), d.strftime("%H:%M:%S %p"))
    d = d + datetime.timedelta(days=6)
    nxt = AppdateTime(d.strftime("%A"),d.strftime("%d %B"), d.strftime("%H:%M:%S %p"))
    return render_template('date.html',today=today, tomorrow=tom, nextday=nxt)
    
@app.after_request
def processResponse(response):
    print("saving in cache")
    cachekey= request.headers.get('X-Cache-Key')
    if(request.method=="GET"):
       cache.set(cachekey,str(response.data).encode("utf8"))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

