Nhớ đổi tên nhá

# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container - or 25032 - công ty
EXPOSE 25032

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py", "--server.port", "25032"]
