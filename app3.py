from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})
    
@app.route('/mojastrona')
def page():
    return "To jest moja strona!"
    
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get("name", "")
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

if __name__ == '__main__':
    app.run(port=5000)
