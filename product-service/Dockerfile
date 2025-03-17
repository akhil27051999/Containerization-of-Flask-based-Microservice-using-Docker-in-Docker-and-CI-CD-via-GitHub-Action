# Step 1: Use a lightweight Python 3.9 base image
# 'slim' variant reduces image size and speeds up build time
FROM python:3.9-slim

# Step 2: Set the working directory inside the container to /app
# All following instructions like COPY and RUN will be executed from this path
WORKDIR /app

# Step 3: Copy the dependency file (requirements.txt) from your local project into the container
COPY requirements.txt .

# Step 4: Install all Python packages listed in requirements.txt
# '--no-cache-dir' helps reduce image size by not caching the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy your main application file (app.py) from your local machine into the container
COPY app.py .

# Step 6: Define the command that will be executed when the container starts
# This starts the Python Flask application
CMD ["python", "app.py"]
