from flask import Flask, request, jsonify
import pickle
import numpy as np

# Carregar o modelo treinado
with open('classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Receber os dados da requisição
    data = request.get_json(force=True)

    # Converter os dados em um array numpy
    input_data = np.array(data['input'])

    # Fazer a previsão usando o modelo carregado
    prediction = model.predict(input_data.reshape(1, -1))

    # Retornar a previsão como uma resposta JSON
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run(port=5000, debug=True)