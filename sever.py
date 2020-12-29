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
        'value': [{'var': result}, {'num': 'niubi'}]
    }


@app.route('/less', methods=['POST'])
def less():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    # result = int(request.json['a']) - int(request.json['b'])
    return {
        'code': 1000,
        'msg': 'success',
        'value': {'userid': 'liekai', 'pwd': '1234567'}
    }


@app.route('/less/niubi', methods=['POST'])
def less_niubi():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    # result = int(request.json['a']) - int(request.json['b'])
    return {
        'code': 1314,
        'msg': 'success',
        'value': '哈哈哈'
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
