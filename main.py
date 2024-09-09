from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

model = joblib.load("trainedModel.pkl")


target_names = ['setosa', 'versicolor', 'virginica']


app = FastAPI()


@app.post("/predict")
async def predict(iris: IrisInput):
    try:
        
        input_features = [[
            iris.sepal_length,
            iris.sepal_width,
            iris.petal_length,
            iris.petal_width
        ]]
        
        
        prediction = model.predict(input_features)
        prediction_class = target_names[prediction[0]]
        
        return {"prediction": prediction_class}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
#2e2c349f-546c-4aa6-9aae-7761406308e6
