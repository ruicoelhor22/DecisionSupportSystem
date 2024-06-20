from flask import Flask, render_template, request, jsonify
import asyncio
import decisionrules
from keys import keys

app = Flask(__name__)

async def solve_decision_rules(data):
    solver = decisionrules.SolverApi(keys.get('SOLVER'))
    response = await solver.solve(decisionrules.SolverType.RULE, keys.get('RESPONSE'), data, "STANDARD", 1)
    return response

@app.route('/')
def index():
    return render_template('index.html', keys=keys)

@app.route('/solve', methods=['POST'])
def solve():
    data = request.form.to_dict()
    data['Lotacao'] = int(data['Lotacao'])
    data['Duração'] = int(data['Duração'])
    response = asyncio.run(solve_decision_rules(data))
    
    if isinstance(response, list) and len(response) > 0:
        response_dict = response[0]
        result = {
            "Preço Diario": response_dict.get("Preço Diario", {}),
            "Preço Final": response_dict.get("Preço Final", {}),
            "Modelo": response_dict.get("Modelo", {})
        }
    else:
        result = {
            "error": "Unexpected response format"
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
 