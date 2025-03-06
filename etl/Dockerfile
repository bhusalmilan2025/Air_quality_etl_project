# Python 3.13 base image
FROM python:3.13-slim

# Setting up working directory
WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# requirements file
COPY requirements.txt .

# Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# project files
COPY . .

# Create directories for data
RUN mkdir -p /tmp/data

# Setting up environment variables
ENV PYTHONPATH=/app
ENV AWS_ACCESS_KEY=${AWS_ACCESS_KEY}
ENV AWS_SECRET_KEY=${AWS_SECRET_KEY}

# Command to run the ETL pipeline
CMD ["python", "etl/etl_pipeline.py"]