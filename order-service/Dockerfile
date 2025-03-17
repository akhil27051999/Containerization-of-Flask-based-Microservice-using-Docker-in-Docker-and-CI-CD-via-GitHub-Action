# Use the official python image 3.9 slim image as the base image
# Slim version reduces image size by removing unnecessary components
FROM python:3.9-slim

# Set the working directory inside the container to /app
# All the following instructions will be relative to this directory
WORKDIR /app

# Copy the requirements.txt file from the host system into the containers /app directory
# It’s a text file that contains a list of packages your Python project needs. Example: flask==2.1.1; requests>=2.25.1; numpy
COPY requirements.txt .

# Install all the dependencies listed in requirements.txt
# '--no-chache-dir' avoids storing downloaded packages in cache, reducing image size
# pip stands for "Pip Installs Packages", and it is the default package manager for Python.
# Using pip install -r requirements.txt, you install all the dependencies in one go.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application file (app.py) from the host system into the container's /app directory
COPY app.py .

# Define the default command to run when the container starts
# This will execute 'python app.py' to start your application
CMD ["python", "app.py"]

