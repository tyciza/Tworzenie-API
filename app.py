from flask import Flask, jsonify, request

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

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get("num1", 0))
        num2 = float(request.args.get("num2", 0))
        result = 1 if (num1 + num2) > 5.8 else 0
        
        return jsonify({
            "prediction": result,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
    except ValueError:
        return jsonify({"error": "Nieprawidłowe dane wejściowe!"}), 400

if __name__ == '__main__':
    app.run(port=5000)
