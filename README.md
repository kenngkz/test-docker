# Demo for Image Dependency
This is a demonstration and test for how image/container dependency might work. container_1 and container_2 both import a function from base.py in the root directory. In order to achieve this, we first build an image with python + base.py, then from this image we build container_1 and container_2.

To run, enter `sh run.sh` in the terminal.

---
# Documentation
## base.py
Contains a function called base_func, which returns a list repeating the given argument 10 times. (eg. base_func("x") > ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x"])

## cont1/c1code.py
Imports base_func from base.py and calls it with the argument "hi". The function call is wrapped in an API.

## cont2/c2code.py
Imports base_func from base.py and calls it with argument 9. The function call is wrapped in an API.

## run.sh
This script should be used to build all images and run both containers. 

On the first line, it builds the base image (the common dependency) and names it test-base. Then on the 2nd line, it builds the images for the 2 containers and runs it according to the docker-compose.yml specifications.

## docker-compose.yml
Specifies the 2 services and containers to run as well as the ports to expose.

## Dockerfile > root directory
This Dockerfile builds the image containing only the base.py file. Any image building from this image will also have access to base.py in the /code directory.

## Dockerfile > cont1
This Dockerfile builds the image for the first container. Building from test-image, it copies the cont1 files into the image and installs the requirements, then finally serves the API in c1code.py using uvicorn to port 8001.

## Dockerfile > cont2
This Dockerfile builds the image for the second container. Building from test-image, it copies the cont2 files into the image and installs the requirements, then finally serves the API in c2code.py using uvicorn to port 8002.

---
# Testing
To test that both containers are working as expected, first run `curl 0.0.0.0:8001`. You should get a json reply {"message":["hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi", "hi"]}. This means container_1 is working. Next, run `curl 0.0.0.0:8002`. You should get a json reply {"message":[9, 9, 9, 9, 9, 9, 9, 9, 9, 9]}. This means container_2 is working.

---
# Upsides
No need to maintain/edit multiple versions of base.py

# Downsides
Intermediate image test-base is not actively used by any container, but it is still taking up memory.
  - We can change the install/run process to first build the relevant images and cleanup the test-base image (via a install file), then seperately run the containers by running a 2nd command (docker-compose...). This solves the above issue, but 1 extra step to deploy from scratch.
  - We can upload test-base to a docker image repository (like docker hub). Currently not sure about implementation + potential authentication/connection issues.

# Notes
We can run any build processes required by all containers while building the test-base image (like `pip install -r requirements.txt`). This will speed up the total build time.

