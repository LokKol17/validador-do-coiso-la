from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Manda um POST pra /validate </h1>", 301

@app.get("/brew_coffee")
def nuh_uh():
    return "<h1><b> TEU C# <b></h1>", 418

@app.post("/validate")
def validate():
    data = request.get_json()

    if not data or 'password' not in data:
        return jsonify({
            "valid": False,
            "message": "tu não colocou exatamente password no campo seu animal"
        }), 400

    password = data.get("password")
    errors = []
    
    if len(password) < 8:
        errors.append('no minimo 8 caracteres')
        
    if re.search(r'\s', password):
        errors.append('zero espaços mano')

    if not re.search(r'[A-Z]', password):
        errors.append('pelo menos 1 letra maiúscula')
        
    if not re.search(r'[a-z]', password):
        errors.append('pelo menos 1 letra minúscula')
        
    if not re.search(r'[0-9]', password):
        errors.append('pelo menos 1 número')

    if errors:
        error_message = f"A senha tem que ter: {', '.join(errors)}."
        return jsonify({
            "valid": False,
            "message": error_message
        }), 400


    return jsonify({
            "valid": True,
            "message": "senha válida"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
