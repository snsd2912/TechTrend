# Use Python 3.8 base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./techtrends /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Initialize the database with predefined posts
RUN python init_db.py

# Expose the application port
EXPOSE 3111

# Command to run the application
CMD ["python", "app.py"]
