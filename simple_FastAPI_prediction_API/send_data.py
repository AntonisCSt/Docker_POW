import requests
import pandas as pd

# Load the input data from day_inference.csv
input_data = pd.read_csv("inference.csv")

# Define the URL of the FastAPI service
url = "http://localhost:8000/predict"  # Update with the correct URL if needed

# Convert the input data to a list of dictionaries
input_data_list = input_data.to_dict(orient="records")

predictions = []

for instance in input_data_list:
    response = requests.post(url, json=instance)
    if response.status_code == 200:
        result = response.json()
        print(result)
        predictions.append(result["predicted_class"])
    else:
        print(f"Prediction failed for instance: {instance}")

print(predictions)
