# Docker Commands

This README provides a quick, step‑by‑step reference for working with **Docker**, **Python containers**, **volume mounting**, **Git**, and building custom Docker images (with `pip` and `uv`).

---

## 1. Verify Docker Installation

Check Docker version:

```bash
docker --version
```

Check if Docker is running:

```bash
docker ps
```

---

## 2. Working with Ubuntu Container

Run an Ubuntu container with bash:

```bash
docker run -it ubuntu bash
```

Update packages inside Ubuntu:

```bash
apt update
```

Exit the container:

```bash
exit
```

---

## 3. Working with Python Docker Image

Run Python container (interactive shell):

```bash
docker run -it python:3.13.1-slim
```

Exit Python shell:

```python
exit()
```

Run Python container with bash:

```bash
docker run -it python:3.13.1-slim bash
```

Check Python version inside container:

```bash
python3 --version
```

---

## 4. Docker Containers & Images Management

List all containers:

```bash
docker ps -a
```

List Docker images:

```bash
docker images
```

Stop all running containers:

```bash
docker stop $(docker ps -aq)
```

Remove all containers:

```bash
docker rm $(docker ps -aq)
```

Remove all Docker images:

```bash
docker rmi -f $(docker images -q)
```

---

## 5. Directory Navigation

Check current directory:

```bash
pwd
```

Go to `test` folder:

```bash
cd test
```

---

## 6. Volume Mounting with Docker

Run Python container with volume mounting:

```bash
docker run -it -v $(pwd)/test:/app/test python:3.13.1-slim bash
```

Run Python pipeline with argument:

```bash
python pipeline.py 5
```

---

## 7. Python Dependencies

Install `pyarrow` (for Parquet support):

```bash
pip install pyarrow
```

Install `uv`:

```bash
pip install uv
```

Create virtual environment with Python 3.13 using `uv`:

```bash
uv init --python=3.13
```

---

## 8. Restarting & Attaching Containers

Start an existing container:

```bash
docker start <container_name>
```

Attach to a running container:

```bash
docker attach <container_name>
```

Exit and stop container:

```text
Ctrl + D
```

Exit container without stopping it:

```text
Ctrl + P + Q
```

---

## 9. Git Commands Workflow

Check status of working directory:

```bash
git status
```

Add all files in `pipeline` folder to staging:

```bash
git add pipeline/
```

Commit changes:

```bash
git commit -m "Added data pipeline script"
```

Pull latest changes from GitHub (main branch):

```bash
git pull --no-rebase origin main
```

Push local commits to GitHub:

```bash
git push origin main
```

View commit history:

```bash
git log --oneline
```

---

## 10. Building & Running Custom Docker Images

### Using pip

Build Docker image:

```bash
docker build -t test:pandas .
```

Run the Docker image:

```bash
docker run -it test:pandas bash
```

Run pipeline inside container:

```bash
python pipeline.py 5
```

---

### Using uv instead of pip

Build Docker image with `uv`:

```bash
docker build -t test:pandas-uv .
```

Run Docker image with argument:

```bash
docker run -it test:pandas-uv 5
```

---

✅ This README serves as a **complete reference** for Docker 
