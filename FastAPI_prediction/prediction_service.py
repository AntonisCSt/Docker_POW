from fastapi import FastAPI
import uvicorn
from loguru import logger
from schema.model_schema import BikeSharingDayDataInputs
from sklearn.ensemble import RandomForestClassifier
from functions.model_functions import ColumnDropper #you need this for the model_pipeline
import joblib
import pandas as pd

app = FastAPI(debug=True)

pickle_file_path = "bike_pipeline_daily_predict.pkl"

loaded_pipeline = joblib.load(pickle_file_path)

@app.get("/")
async def root():
    return {"message": "Hello use /predict for the model prediction"}

@app.post("/predict", status_code=200)
async def predict(input_data: BikeSharingDayDataInputs):
    """
    make prediction from model
    """
    logger.info(f"Making prediction on inputs: {input_data}")
    logger.info(f"Type of input: {type(input_data)} ")
    
    input_dict = input_data.model_dump()
    # Create a DataFrame from the input dictionary
    df_input_data = pd.DataFrame([input_dict])

    logger.info(f"inputs dataframe: {df_input_data}")

    targets = df_input_data['cnt']
    df_input = df_input_data.drop('cnt',axis=1,inplace=False)
    predictions = loaded_pipeline.predict(df_input)

    results = {
            "predictions": predictions.tolist(),  # type: ignore
            "version": '0.0.1',
            "actual_targets": targets.tolist() # this is important because the output needs to be jasonable
        }
    
    logger.info(f"Prediction results: {results}")
    return results

if __name__ == '__main__':
    uvicorn.run(app)