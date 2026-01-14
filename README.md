# DataEngineering-Docker
WorkShop Codespaces

# Check docker version
docker --version

# Check docker is running
docker ps

# Run ubuntu container with bash
docker run -it ubuntu bash

# Update packages inside ubuntu
apt update

# Exit container
exit

# Run python docker image
docker run -it python:3.13.1-slim

# Exit python shell
exit()

# Run python image with bash
docker run -it python:3.13.1-slim bash

# List all containers
docker ps -a

# List docker images
docker images

# Stop all containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all docker images
docker rmi -f $(docker images -q)

# Check current directory
pwd

# Go to test folder
cd test

# Run python container with volume mounting
docker run -it -v $(pwd)/test:/app/test python:3.13.1-slim bash

# Run python pipeline with argument
python pipeline.py 5

# Install pyarrow (for parquet support)
pip install pyarrow

# Install uv
pip install uv

# Create virtual environment with Python 3.13 using uv
uv init --python=3.13

