from flask import Flask, request

app = Flask("my-app")


@app.route('/add', methods=['GET'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a'] + request.json['b']
    return {
        'code': 0,
        'msg': 'ok',
        'value': result
    }


@app.route('/less', methods=['POST'])
def less():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = int(request.json['a']) - int(request.json['b'])
    return {
        'code': 1000,
        'msg': 'success',
        'value': result
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
