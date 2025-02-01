# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app

# Command to run your application (modify as needed)
CMD ["python", "main.py"]