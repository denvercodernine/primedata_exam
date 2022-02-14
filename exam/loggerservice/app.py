# flask_web/app.py

from datetime import datetime
import os.path

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return str(datetime.now())

@app.route('/recordlog', methods=['POST'])
def recordlog():
    
    app.logger.info('Logging request recieved')

    if request.method == 'POST':
        time = request.form.get('time')

    with open('usage.log', 'a') as f:
        f.write(time)
        f.write('\n')
        app.logger.info('Logged')
    return "200 OK"

@app.route('/usage.log', methods=['GET'])
def usage():
    content = ''
    with open('usage.log', 'r') as f:
        content = f.readlines()
    text = ''
    for line in content:
        text = text + line + '<br>'
    return text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8081)
