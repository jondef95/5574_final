# ECE 5574 Final Project - Team1 
# Random Fact Generator

This contribution to the team project contains the Python-Flask server that serves the API for random fact generation. The front-end will eventually contain only two entrypoints, both GET commands. One command will return a random fact, and another will attempt to find a fact about the topic that is input by the user. 

## Running the Code
For the time being, the API itself has not been implemented. However, the backend code that scrapes Wikipedia has been. The tests written demonstrate the use of this code. 

To run the current tests, please download the Docker Image at https://hub.docker.com/r/jondef95/fact_gen_test/ and run the image. It will automatically run the tests given. Alternatively, you can build the image using the Dockerfile in this repository.
