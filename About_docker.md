
Was there ever a need for sending your code to another computer/laptop to run it? Or the opposite, had to run someone's else code. You obviously needed a requerements.txt file in order to have the same library versions.

Consider another situation where you're working on a Windows machine, and your colleague is using macOS. Your code might rely on certain OS-specific functionality, and running it on a different OS could lead to errors. With Docker, you can build your application within a container that matches your desired operating system environment. Your colleague can then run the same container on their macOS machine without any OS-related issues.

Docker ensures that your code runs consistently across different systems, sparing you from the frustration of debugging compatibility problems and allowing you to focus on what matters most: your data science work.

## So what is docker?

Docker is a tool that allows you to package your code, along with all its dependencies, into a self-contained unit called a "container." These containers are isolated environments that encapsulate everything needed to run your application, from libraries to configurations, in a consistent and reproducible manner.

## Install docker

https://docs.docker.com/engine/install/

## Let's run our first example

To have a docker container you need to have a docker image. A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments. You choose when to run an image and that iamge is then converted to a container. So a container is basically a docker image that is running/active.

Finnally, to create an image you need to have a set of instructions written in a special file called. Dockerfile. Look at this example:

```Dockerfile
# Use a lightweight base image
FROM debian:11-slim

# Run a simple command to print "Hello, World!"
CMD ["echo", "Hello, World!"]
```

`FROM debian:11-slim`: This line specifies the base image for your Docker container. It uses Debian Linux version 11-slim as the base image. Debian is a Linux distribution that's composed entirely of free and open-source software and this version is considered lightweighted.

`CMD ["echo", "Hello, World!"]`: This line is the command that will be executed when you run a container from the image. In this case, it's a simple echo command that prints "Hello, World!" to the standard output (stdout).

command build the image:

```terminal
docker build -t alpine-hello-world .
```

This tags your image with the name "alpine-hello-world" so you can easily reference it later.

```terminal
docker run alpine-hello-world
```

This command will execute the CMD instruction in the Dockerfile, which runs the echo command, and you will see the output "Hello, World!" printed to the terminal.

That's it! You've successfully built and run a Docker container that prints "Hello, World!" using Alpine Linux as the base image.

## Docker running python

Let's see the following example:

```Dockerfile
# Use a lightweight python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your Python script into the container
COPY hello.py .

# Run the Python script
CMD ["python", "hello.py"]
```

To build it and run it we use the following commands:

`docker build -t python-hello-world .`

`docker run python-hello-world`

Here we use `python:3.10-slim` as our base image to run hello.py scirpt that is local.

We first create a working directory `/app`
Then copy the local file `hello.py` to the destination `/.` of our docker image.

Finnaly, we run the command we seen previously.

What is cool here to unserstand about docker, is that the base image here is python:3.10-slim. When we set this as base image, this image itself has other previous base images to make python run, especially in a slim (lightweighted) enviroment. This particular image runs on the debian Linux distribution that we saw in the previous example: https://hub.docker.com/layers/library/python/3.10-slim/images/sha256-0d15918ecae76250659ae3036ad1fc898f801f6cb803860bdf0cc4b27fe316dc

and here is the actual dockerfile: https://github.com/docker-library/python/blob/39ee37caebef9628f3b906b8b778d467eb32005f/3.10/slim-bullseye/Dockerfile

You might not understand many commands, but its fine. Try to get the general concept.

So, when we use one image, we might actually downloading and installing other ones as well that set the base.

Now lets take a look at some useful commands:

* `RUN`

Install any necessary Python dependencies (if needed)
`RUN pip install -r requirements.txt`

RUN is used to execute commands during the image building process

It is typically used for actions that modify the container's filesystem, such as installing packages, setting up environment variables, or performing any other setup tasks.

if you want to run multiple commands: 
`RUN apt-get update && apt-get install -y package_name`

* `CMD`

CMD is used to specify the default command that should be run when a container is started from the image. If you have multiple CMD instructions, only the last one will take effect.

* `EXPOSE`

EXPOSE 8080: If your Python script listens on a network port (e.g., for a web server), you can expose that port using this line. Remember to update the port number accordingly.

* `ENV`

ENV MY_VARIABLE=my_value: If your Python script relies on environment variables, you can set them using this line.

* `VOLUME`

In the context of Docker, a volume is a persistent storage location that exists outside of the container. Volumes are useful for storing data that needs to persist even if the container is stopped or removed.

Example with volume:

`docker run -v absolute_path_to_your_folder:data -it app_with_volumes`

on ubuntu related OS you can use:
`pwd/yourfolder`

Otherwisem, on windows you have to copy thw full path.

-it runs the container on interactive mode. (means that you can write commands after that).
However, if you include a CMD command, it will not run on the interactive mode and just use the last CMD command you have.

with nano we can edit the volume files, edit them delete the container and then again create a new one with the same volume. You will see that the volume was edited!

# Converting our FAST API into an image

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

COPY requirements.txt .

# Expose the port that FastAPI will run on
EXPOSE 80

RUN pip install -r requirements.txt

CMD ["uvicorn", "prediction_service:app","--reload", "--host", "0.0.0.0", "--port", "80"]

```

cd inside the excersice FASTAPI folder:

`docker build -t fast_api .`

`docker run -v [your absolute_path]\Docker\excersice_FASTapi\volume_data:/app/volume_data -p 8000:80 fast_api`

Use http://localhost:8000/ from your machine, if you get http error connection.

to test it use the UI swagger at http://localhost:8000/docs

also run send_data.py
expected correct answer: [[3129], [3163], [3163], [3163]]
