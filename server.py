from flask import Flask, request

app = Flask(__name__)


@app.route('/v1/validate', methods=['POST'])
def index():
    print(request.headers)
    body = request.get_json()
    return "Hello World"


if __name__  == '__main__':
    app.run(debug=True)


