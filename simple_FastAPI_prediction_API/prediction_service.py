from fastapi import FastAPI
import pandas as pd
import joblib
from pydantic import BaseModel

app = FastAPI()
# Load the trained model from a file
loaded_model = joblib.load('iris_model/iris_rf_model.pkl')


@app.get("/")
async def root():
    return {"message": "Hello, use predict for the iris model prediction"}

@app.post("/predict")
async def predict(input_data: dict, status_code=200):
    try:
        input_dict = input_data
        df_input_data = pd.DataFrame([input_dict])
        prediction = loaded_model.predict(df_input_data)
        results = {
            "predicted_class": prediction.tolist(),
            "version": '0.0.1',
        }
        return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
