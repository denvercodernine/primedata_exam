# flask_web/app.py

from datetime import datetime
import requests

from flask import Flask
app = Flask(__name__)

url = 'http://192.168.1.11:8081/recordlog'


@app.route('/')
def hello_world():
    a = "Time is "
    a = a + datetime.now().strftime('%a %b %d %Y %H:%M:%S %Z%z (UTC)')
    try:
        myobj = {'time': datetime.now().strftime('%a %b %d %Y %H:%M:%S %Z%z (UTC)')}
        requests.post(url, data = myobj)
    except:
        app.logger.info('Request send failure')
        pass
    return a


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
