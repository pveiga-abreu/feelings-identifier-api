from flask import jsonify, request
from unidecode import unidecode
from string import punctuation
import numpy as np
import pickle
import nltk

from app.errors import InvalidRequest, InternalError
from app.validators import validate_predict

model = pickle.load(open('app/models/model.pickle', 'rb'))
vectorizer = pickle.load(open('app/models/vectorizer.pickle', 'rb'))

stop_words = (
    [ unidecode(w).lower() for w in nltk.corpus.stopwords.words('portuguese') ]
    +
    list(punctuation)
    )

wpt_tokenizer = nltk.tokenize.WordPunctTokenizer()
stemmer = nltk.RSLPStemmer()

def make_predict():
    payload = request.get_json()
    err = validate_predict(request)
    if err: raise InvalidRequest(err[0])

    try:
        text = payload['text']

        text = _normalize_text(text)

        prevision = model.predict(text)

    except:
        raise InternalError('Internal Error')

    else:
        return jsonify({
            'response': 'positive' if bool(prevision[0]) else 'negative'
        })

def _normalize_text(text: str) -> np.array:
    text = unidecode(text).lower()
    text = ' '.join([ stemmer.stem(word) for word in wpt_tokenizer.tokenize(text) if word not in stop_words ])
    text = np.array([text])
    text = vectorizer.transform(text)
    return text
