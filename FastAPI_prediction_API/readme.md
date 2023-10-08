# Fast API docker example

From the Restful API project we copy the folcers and files:

* `/schema`: the pydantic schema that is used by the FAST API app
* `/functions`: the functions that are needed in the sklearn pipeline that is used by the FAST API app
* `prediction_service.py` : python script that run the FAST API app
* `send_data.py` : we are going to use this to test the docker container with the FAST API app.
* `day_inference.csv`

we also create a volume_data and add the model. The idea behind it is that I can have persisent volume that I can change the model independtly from the different changes that can happen in the app inside docker.

Important: Make sure you have the folder functions/ else you get attribute error column ( for issue:`AttributeError: Can't get attribute 'ColumnDropper'`)

We create a dockerfile:

```Dockerfile
# Use a lightweight python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Define the volume mount point (this is where the data from the host will be mounted)
VOLUME /app/volume_data

COPY schema schema
COPY functions functions
COPY prediction_service.py .
COPY bike_pipeline_daily_predict.pkl

COPY requirements.txt .

# Expose the port that FastAPI will run on
EXPOSE 80

RUN pip install -r requirements.txt

CMD ["uvicorn", "prediction_service:app","--reload", "--host", "0.0.0.0", "--port", "80"]

```

cd inside the excersice FASTAPI folder:

`docker build -t fast_api .`

`docker run -p 8000:80 fast_api`

Use http://localhost:8000/ from your machine, if you get http error connection.

to test it use the UI swagger at http://localhost:8000/docs

also run send_data.py
expected correct answer: [[3129], [3163], [3163], [3163]]
