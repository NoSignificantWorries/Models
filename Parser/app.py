import subprocess

import flask

import writePSQL as psql

app = flask.Flask(__name__)

@app.route("/api/parser")
def parsing():
    product_arg = flask.request.args.get("product")
    pages_arg = flask.request.args.get("pages_count")
    args = []
    if product_arg:
        args += ["-p", product_arg]
    if pages_arg:
        args += ["-c", pages_arg]
    
    try:
        subprocess.run(["python3", "main.py"] + args)
    except BaseException as error:
        return "Unexpected errors occured!\n", 500
    return "Parsing done.", 200

@app.route("/api/data")
def get_data():
    try:
        psql_client = psql.PSQLwriter("dmitry", "parserdb", "products")
        json_data = psql_client.write_data_to_json(None) 
    except BaseException as error:
        return "Unexpected errors occured!\n", 500
    return flask.Response(json_data, mimetype='application/json')

@app.route("/api/clear")
def clear():
    try:
        psql_client = psql.PSQLwriter("dmitry", "parserdb", "products")
        psql_client.clear_table()
    except BaseException as error:
        return "Unexpected errors occured!\n", 500
    return "Table succesfully cleaned.\n", 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

