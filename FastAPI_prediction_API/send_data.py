import requests
import pandas as pd

# Load the input data from day_inference.csv
input_data = pd.read_csv("day_inference.csv")

# Define the URL of the FastAPI service
url = "http://localhost:8000/predict"  # Update with the correct URL if needed

# Convert the input data to a list of dictionaries
input_data_list = input_data.to_dict(orient="records")

# Make POST requests for each input data instance
predictions = []

for instance in input_data_list:
    response = requests.post(url, json=instance)
    if response.status_code == 200:
        result = response.json()
        predictions.append(result["predictions"])
    else:
        print(f"Prediction failed for instance: {instance}")

# predictions now contains the model's predictions for each input data instance
print(predictions)
