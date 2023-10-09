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