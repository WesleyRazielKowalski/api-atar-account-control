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
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST', 'PUT'])
def control_account():
    try:
        if request.headers['Authorization']:
            if Authentication.check_can_access(request.headers['Authorization']):
                if request.method == 'POST':
                    return_id = AccountControlObj.control_insert(request)
                    if return_id:
                        result_json = return_id
                elif request.args.get("id"):
                    param_id = request.args.get("id")
                    if request.method == 'GET':
                        result_json = AccountControlObj.control_get(param_id)
                    elif request.method == 'PUT':
                        result_json = AccountControlObj.control_update(request, param_id)

                # Trata o retorno dos métodos POST, PUT, GET
                result_status = result_json[1]
                result_json = result_json[0]
                return_dump = json.dumps(result_json, ensure_ascii=False)
                return Response(return_dump, content_type="application/json; charset=utf-8"), result_status
            else:
                # Tem o header de autorização, mas não está com a chave correta.
                result_json = {"erro": " Não autorizado", "descrição": "Chave de autenticação inválida"}
                return_dump = json.dumps(result_json, ensure_ascii=False)
                return Response(return_dump, content_type="application/json; charset=utf-8"), 401
        else:
            # Não tem o header de autorização
            result_json = {"erro" : " Não autorizado", "descrição" : "Não foi informado a chave de autenticação"}
            return_dump = json.dumps(result_json, ensure_ascii=False)
            return Response(return_dump, content_type="application/json; charset=utf-8"), 401
    except Exception as e:
        logging.info(str(e))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)