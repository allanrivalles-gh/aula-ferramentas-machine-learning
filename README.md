# aula-ferramentas-machine-learning

Este repositório contém um exemplo simples de como treinar um modelo com Scikit learn e carregar este modelo em um servidor Flask para fazer predições via requisições Restful.

Passo a passo para utilizar:

* Tenha instalado o Python

1) Criar um ambiente virutal python:

    * python -m .venv venv

2) Ative o embiente virtual:

* Linux/Mac
  * source .venv/bin/activate
* Windows
    * .venv/Scripts/activate

3) Execute as celulas do notebook model_train.ipynb para gerar um modelo treinado

4) Rode a aplicação flask:
    * python flask_app.py
    
5) Abra o postman e crie uma request POST para a url: http://127.0.0.1:5000/predict e um body raw json com um dos exemplos do arquivo sample_input.json.

6) Clique em send para mandar a requisição e receber a response com um inteiro representando a classe predita.