# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /myapp

# Copy the current directory contents into the container at /app
COPY . /myapp/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run server when the container launches (can be overridden by docker-compose)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
