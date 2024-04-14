# # this is new corrected fast api file as per changes for UI (for front end)
from fastapi import FastAPI, Request,HTTPException
from fastapi.responses import HTMLResponse
from muffin_vs_cupcake import muffin_vs_cupcake
import pickle
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount the static directory for serving CSS and JavaScript file
app.mount("/static", StaticFiles(directory=Path(__file__).parent/ "static"), name="static")


pickle_in=open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# Serve the HTML file

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return open("index.html").read()

# Endpoint to handle prediction
@app.post('/predict')
async def predict_species(data: muffin_vs_cupcake):
    data = data.dict()

    print("data====", data)

    flour = data['flour']
    sugar = data['sugar']

    prediction = classifier.predict([[flour, sugar]])

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

# Run: uvicorn NewApp:app --reload