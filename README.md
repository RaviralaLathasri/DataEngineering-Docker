Data Engineering Basics with Docker, Python & uv

This project demonstrates basic data engineering concepts using Docker, Python, command-line arguments, Parquet files, and uv for virtual environments.

1. What is Docker?

Docker is a tool used to run applications in isolated containers.

Why Docker in Data Engineering?

Same environment everywhere

Easy setup of tools (Python, Spark, DBs)

No dependency conflicts

Used for ETL pipelines and deployment

2. Basic Docker Commands Used
# Check docker version
docker --version

# Check docker is running
docker ps

# Run Ubuntu container with bash
docker run -it ubuntu bash

# Update packages inside ubuntu
apt update

# Exit container
exit

3. Running Python using Docker
# Run Python image
docker run -it python:3.13.1-slim


This opens the Python shell:

>>>


Exit Python:

exit()

4. Running Bash inside Python Docker Image
docker run -it python:3.13.1-slim bash


This opens a Linux bash shell inside the container.

5. Docker Images and Containers
# List all images
docker images

# List all containers (running + stopped)
docker ps -a

Delete all containers and images
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images -q)

6. Linux Basic Commands
pwd        # shows current directory
ls         # list files and folders
cd test    # move into test folder
cd ..      # go back

7. Volume Mounting in Docker
docker run -it -v $(pwd)/test:/app/test python:3.13.1-slim bash

Meaning:

$(pwd)/test → local folder

/app/test → folder inside container

Both folders are linked

Changes reflect on both sides.

8. Data Pipeline Using Python
pipeline.py
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

9. Running the Pipeline
python pipeline.py 5

Explanation:

5 is the input (day)

sys.argv[1] reads this value

Output file:

output_day_5.parquet

10. Parquet Error & Fix
Error:
Missing optional dependency 'pyarrow'

Fix:
pip install pyarrow


Parquet format needs pyarrow or fastparquet.

11. What is uv?

uv is a fast Python package manager and virtual environment tool.

Why uv?

Faster than pip

Cleaner dependency management

Modern tool used in industry

12. uv Commands Used
# Install uv
pip install uv

# Create virtual environment with Python 3.13
uv init --python=3.13

What this does:

Creates .venv/

Uses Python 3.13

Generates pyproject.toml

❌ Does NOT install Python globally
✅ Python is only inside the project environment

13. Installing Packages Using uv
uv pip install pandas pyarrow

14. pip vs uv
pip	uv
Slower	Faster
Old tool	Modern tool
Manual venv	Auto venv
Basic	Industry-ready

