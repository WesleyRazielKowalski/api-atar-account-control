import datetime
from flask import Flask, request, json, Response, render_template
#import flask
import logging
from control_account import AccountControlObj
from authentication import Authentication
import base64

from flask import Flask, render_template
#from flask_basicauth import BasicAuth

app = Flask(__name__)

@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

@app.route('/register', methods=['GET', 'POST', 'PUT'])
def control_account():
    try:
        if request.headers['Authorization']:
            if Authentication.check_can_access(request.headers['Authorization']):
                if request.method == 'GET':
                    return AccountControlObj.get(request)
                elif request.method == 'POST':
                    return AccountControlObj.insert(request)
                elif request.method == 'PUT':
                    return AccountControlObj.update(request)
        else:
            return "informe o token"
    except:
        logging.info("e")

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)