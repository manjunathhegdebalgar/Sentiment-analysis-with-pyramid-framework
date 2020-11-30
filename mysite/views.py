import json
import pickle

import joblib
import numpy as np
from pyramid.view import view_config

# Loading the pretrained saved models to use
loaded_model = joblib.load("./nlpmodels/model.pkl")
loaded_stop = joblib.load("./nlpmodels/stopwords.pkl")
loaded_vec = joblib.load("./nlpmodels/vectorizer.pkl")


def classify(statement):
    """This module does the prediction."""
    label = {"negative": "negative", "positive": "positive"}
    X = loaded_vec.transform([statement])
    y = loaded_model.predict(X)[0]
    proba = np.max(loaded_model.predict_proba(X))
    return label[y], proba


class MySite:
    def __init__(self, request):
        self.request = request
        print(request.referer)

    @view_config(route_name="home", renderer="templates/home.jinja2")
    def home(self):
        """This is the home page of our application as it appears in the beginning."""
        return dict()

    @view_config(route_name="home", renderer="json", request_method="POST")
    def review(self):
        """This is the view obtained after changes are encountered in the home page."""
        # Getting the review typed inside the input box having id = review. Refer templates/home.jinja2
        typed_review = self.request.json_body.get("review")
        # Passing entered review to the classify() method
        classified = classify(typed_review)
        # The returned tuple contains predicted class and probability. Following lines fetch each of them.
        predicted_class = classified[0]
        # The confidence will be a numpy float and the following lines convert them to native python float.
        probability_in_numpy = classified[1]
        probability_native_python = probability_in_numpy.item()
        # Getting the percentage out of probability
        probability = probability_native_python * 100
        probability = round(probability, 2)
        # Converting float to string inorder to render it on the page.
        str_probability = str(probability)
        response = {
            "sentiment": predicted_class,
            "probability": str_probability,
        }
        # Passing the response as a json object to the Javascript file.
        json_response = json.dumps(response)
        json_object = json.loads(json_response)
        return json_object
