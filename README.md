# ECE 5574 Final Project - Team1 
# Random Fact Generator

This contribution to the team project contains the Python-Flask server that serves the API for random fact generation. The front-end will eventually contain only two entrypoints, both GET commands. One command will return a random fact, and another will attempt to find a fact about the topic that is input by the user. 

## Running the Code
There are two Docker images currently available to run:

### Without Authentication
To run an image without authentication, either download the [Docker Image](https://hub.docker.com/r/fact-gen-server) by running the commands:
`sudo docker run -p 8080:8080 jondef95/fact-gen-server`

or use the Dockerfile in the api-server directory:
`sudo docker build -t fact-gen-server api-server/`
`sudo docker run -p 8080:8080 fact-gen-server`

### With Authentication
To run an image of the fact generator with authentication, either download the [Docker Image](https://hub.docker.com/r/factauth_web) by running the commands:
`sudo docker run -p 8000:8000 jondef95/factauth_web`

or use the Docker-Compose file in the Fact_Auth directory:
`sudo docker-compose up Fact_Auth/`

## Running the Tests
To run the current tests, please download the [Docker Image](https://hub.docker.com/r/jondef95/fact_gen_test/) and run the image. It will automatically run the tests given. Alternatively, you can build the image using the Dockerfile in this repository.
