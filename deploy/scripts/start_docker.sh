#!/bin/bash
# Login to AWS ECR
aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 843369994444.dkr.ecr.eu-north-1.amazonaws.com/text-classification:v3

# Pull the latest image
docker pull 843369994444.dkr.ecr.eu-north-1.amazonaws.com/text-classification:v3

# Check if the container 'campusx-app' is running
if [ "$(docker ps -q -f name=text-classification)" ]; then
    # Stop the running container
    docker stop text-classification
fi

# Check if the container 'campusx-app' exists (stopped or running)
if [ "$(docker ps -aq -f name=text-classification)" ]; then
    # Remove the container if it exists
    docker rm text-classification
fi

# Run a new container
docker run -d -p 80:5000 -e DAGSHUB_PAT=319a47e590ec9cc01014f4b6e8805468766d0757 --name text-classification 843369994444.dkr.ecr.eu-north-1.amazonaws.com/text-classification:v3