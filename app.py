from flask import Flask
from flask_restful import Api
from sentiment_analyser import sentimentAnalyser

app = Flask(__name__)
api = Api(app)

api.add_resource(sentimentAnalyser, '/analyze-sentiment')

if __name__ == "__main__":
    app.run(port=5000, debug=True)