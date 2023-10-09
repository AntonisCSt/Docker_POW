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