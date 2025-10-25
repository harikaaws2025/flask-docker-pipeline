# Base image
FROM python:3.9-slim

# Working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose Flask app port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
