import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from flask_restful import Resource,reqparse

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

parser = reqparse.RequestParser()
parser.add_argument('review', type=str)

class sentimentAnalyser(Resource):
    def get(self):
        args = parser.parse_args()
        review = args['review']

        doc = nlp(review)

        return {
            'score': doc._.polarity
        }

