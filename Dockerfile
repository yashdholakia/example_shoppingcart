# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pytest

# Make port 80 available to the world outside this container
EXPOSE 80

# Run tests and start the service when the container launches
CMD  ["python", "shopping.py" , "AABB"]
