from flask import Flask #pip install flask
from flask_restful import Api, Resource,reqparse #pip install flask-restful
from model import predict_class



app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self):
        return {"info":"Some info"}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("text",type=str)
        text = parser.parse_args()['text']
        prediction = predict_class(text)
        return prediction

api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000,host='127.0.0.1')
"""
ЛР API

- сохраняете обученную модель в файл (можно использовать модели с лаб по классификации текста и картинок)
- делаете api с POST-методом для получения новых прогнозов
- + один любой метод (кроме вывода информации о модели)

"""