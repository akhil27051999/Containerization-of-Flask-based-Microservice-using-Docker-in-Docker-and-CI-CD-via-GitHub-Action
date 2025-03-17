# Use the official lightweight Python 3.9 image as the base image
# 'slim' version contains only minimal packages to keep the image small
FROM python:3.9-slim

# Set the working directory inside the container to /app
# All following commands will execute in this directory
WORKDIR /app

# Copy the requirements.txt file (which contains all dependencies) from your local machine to the container
COPY requirements.txt .

# Install the dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Copy your main application file (e.g., app.py) into the container's working directory
COPY app.py .

# Set the default command to run the Flask application when the container starts
CMD ["python", "app.py"]
