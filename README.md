Data Engineering Basics with Docker, Python and uv

This project explains basic data engineering concepts using Docker, Python, command-line arguments, Parquet files and uv virtual environments.

What is Docker?

Docker is a tool used to run applications inside isolated containers.
It helps us run the same code with the same environment everywhere.

Why Docker is used in Data Engineering:

Same environment on laptop, server and cloud

Easy setup of tools like Python, Spark, Databases

No dependency conflicts

Reliable data pipelines

Basic Docker Commands Used

docker --version
Checks Docker version

docker ps
Checks whether Docker is running

docker run -it ubuntu bash
Runs an Ubuntu container and opens bash shell

apt update
Updates package list inside the container

exit
Exits the container

Running Python using Docker

docker run -it python:3.13.1-slim

This opens the Python shell directly.

To exit Python shell:
exit()

Running bash inside Python Docker image

docker run -it python:3.13.1-slim bash

This opens Linux bash inside the Python container.

Docker Images and Containers

docker images
Lists all Docker images

docker ps -a
Lists all containers (running and stopped)

Delete all containers and images:

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images -q)

Basic Linux Commands

pwd
Shows current directory

ls
Lists files and folders

cd test
Moves into test folder

cd ..
Moves back to parent folder

Docker Volume Mounting

docker run -it -v $(pwd)/test:/app/test python:3.13.1-slim bash

This connects local folder "test" to "/app/test" inside the container.
Any file change in local folder is reflected inside container and vice versa.

Data Pipeline using Python

pipeline.py file:

import sys
import pandas as pd

if len(sys.argv) < 2:
print("Usage: python pipeline.py <day>")
sys.exit(1)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df = pd.DataFrame({
"A": [1, 2],
"B": [3, 4]
})

print(df)

output_file = f"output_day_{day}.parquet"
df.to_parquet(output_file)

print(f"Pipeline completed. File saved as {output_file}")

Running the Pipeline

python pipeline.py 5

Here:

5 is the input value (day)

sys.argv[1] reads this value

Output file created: output_day_5.parquet

Parquet Error and Fix

Error occurs because pandas alone cannot write parquet files.

Fix:
pip install pyarrow

pyarrow is required to read/write parquet files.

What is uv?

uv is a fast Python package manager and virtual environment tool.
It is a modern replacement for pip and venv.

Why uv is used:

Very fast package installation

Clean dependency management

Separate environment per project

Used in industry

uv Commands Used

pip install uv
Installs uv tool

uv init --python=3.13
Creates a virtual environment using Python 3.13

This creates:

.venv folder

pyproject.toml file

Python is installed only inside the project, not globally.

Installing packages using uv

uv pip install pandas pyarrow

This is faster than pip install.

Final Summary
