Here the dockerfile contains:

```Dockerfile
# Use a lightweight python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

COPY prediction_service.py .

COPY requirements.txt .

COPY iris_model .

# Expose the port that FastAPI will run on
EXPOSE 80

RUN pip install -r requirements.txt

CMD ["uvicorn", "prediction_service:app","--reload", "--host", "0.0.0.0", "--port", "80"]
```

`docker build -t fast_api .`

`docker run -p 8000:80 fast_api`

Use http://localhost:8000/ from your machine, if you get http error connection.

and run:

`python send_data.py`

You can also go to the page: `http://localhost:8000/docs` and run your own examples!

example to use for FastAPI's Swagger UI:

```python
{
    'sepal length (cm)':5.1,
    'sepal width (cm)':3.5,
    'petal length (cm)':1.4,
    'petal width (cm)':0.2
}
```
