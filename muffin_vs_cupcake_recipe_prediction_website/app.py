"""
Created on 14th April 2024

@author: Rijwan
"""
# 1 Library imports

import uvicorn
from fastapi import FastAPI
from muffin_vs_cupcake import muffin_vs_cupcake
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object

app = FastAPI()

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

# 3.Index route, open automatically on http://127.0.0.1:8000

@app.get('/')
def index():
    return {'message': 'Hello, stranger'}

#4. Expose the prediction functionality, make a prediction from the passed
#   JSON data and return the predicted muffine_vs_cupcake_recipes with the confidence

@app.post('/predict')
def predict_recipes(data:muffin_vs_cupcake):
    data = data.dict()

    print("data====", data)

    flour =data['flour']
    sugar= data['sugar']

    prediction = classifier.predict([[flour,sugar]])

    print('Prediction===', prediction)

    # Create a code to guesss when a recipes is a muffin or a cupcake

    if (classifier.predict([[flour, sugar]])) == 1:
        prediction = 'You\'re looking at a muffin recipe!'
        print('You\'re looking at a muffin recipe!')
    else:
        prediction ='You\'re looking at a cupcake recipe!'
        print('You\'re looking at a cupcake recipe!')
    return{
        'prediction': prediction
    }
# 5. Run the API with uvicorn
# Will run on http://127.0.0.1:8000

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload



