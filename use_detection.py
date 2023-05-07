from tensorflow import keras
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.corpus import stopwords
import nltk
from scipy.stats import boxcox


# Laden des Tokenizers aus der JSON-Datei

def predict(text):
    nltk.download("stopwords")

    stop_words = stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

    model = keras.models.load_model('./fake-news-model/mein_model.h5')
    out = []
    with open('tokenizer.json', 'r', encoding='utf-8') as f:
        tokenizer_json = f.read()
    tokenizer = tokenizer_from_json(tokenizer_json)
    result = []
    for article in text:
        for token in gensim.utils.simple_preprocess(str(article)):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3 and token not in stop_words:
                result.append(token)

        x = tokenizer.texts_to_sequences(result)
        x = pad_sequences(x, maxlen = 40, truncating = 'post')
        x = x.reshape(1,-1)
        out.append(model.predict(x))
    out = np.array(out).reshape(-1)
    transformed_probs = boxcox(out)[0]
    scaled_probs = (transformed_probs - np.min(transformed_probs)) / (np.max(transformed_probs) - np.min(transformed_probs))

    return (scaled_probs*0.9)+0.05


print(predict([['test'],['test number 2.50'], ['test3']]))
