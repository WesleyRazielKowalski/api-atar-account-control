import datetime
from flask import Flask, request, json, Response, render_template
import logging
from account_control import AccountControlObj
from authentication import Authentication
import base64

from flask import Flask, render_template

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
                if request.method == 'POST':
                    return_id = str(AccountControlObj.control_insert(request))
                    if return_id:
                        result_json = {"id": str(return_id)}
                        return_dump = json.dumps(result_json, ensure_ascii=False)
                        return Response(return_dump, content_type="application/json; charset=utf-8")
                elif request.args.get("id"):
                    param_id = request.args.get("id")
                    if request.method == 'GET':
                        return AccountControlObj.control_get(param_id)
                    elif request.method == 'PUT':
                        return AccountControlObj.control_update(request, param_id)

            return "Sem erros"
    except:
        logging.info("e")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)