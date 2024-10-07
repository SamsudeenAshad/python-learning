from fastapi import FastAPI
from pydantic import BaseModel , field_validator , Field
from model_inference import predict_co2_level

app = FastAPI()

class Co2Prediction(BaseModel):
    start_date : str
    end_date : str 


@app.post("/get-co2-level-prediction")
async def get_co2_level(request:Co2Prediction):
    co2_prediction  = predict_co2_level(start_date=request.start_date , end_date=request.end_date)
    return {
        "co2_prediction" : co2_prediction
    }
   