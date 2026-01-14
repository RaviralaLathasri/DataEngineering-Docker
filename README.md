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

#check python version in docker
python3 --version

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

# TO start the same container
docker start <container_name>

#Entering to container if container alredy runs in background
docker attach <container_name>

#Container exit + stop
Ctrl + D

#Exit only, container run avuthundi
Ctrl + P + Q


# Check current status of working directory(Shows files that are modified, staged, or untracked)
git status

Add all files in 'pipeline' folder to staging area(Prepares files for commit)
git add pipeline/

Commit staged changes to local repository(Saves changes in history with a message)
git commit -m "Added data pipeline script"

# Fetch and merge remote changes from GitHub main branch(Sync local repository with remote to avoid conflicts)
git pull --no-rebase origin main

# Push local commits to GitHub(Updates remote main branch with your changes)
git push origin main


#  View short commit history(Shows recent commits, merge commits, and messages)
git log --oneline

# Build custom Docker image for pipeline
docker build -t test:pandas 

# Run the created Docker image in interactive mode
docker run -it test:pandas bash

# Run the file inside the docker 
python pipeline.py 5

# creating Docker using uv insted of pip
docker build -t test:pandas-uv .

# Run docker image uv
docker run -it test:pandas-uv 5



