# Use the smallest possible Debian-based image with Python
FROM python:3.10-slim

# Set a working directory
WORKDIR /app
RUN pip3 install requests