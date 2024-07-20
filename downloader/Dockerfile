FROM python:3.10-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    build-essential \
    zlib1g-dev \
    libssl-dev \
    libtool \
    && rm -rf /var/lib/apt/lists/*

# Install HTTrack
RUN wget https://mirror.httrack.com/historical/httrack-3.49.2.tar.gz \
    && tar -xvzf httrack-3.49.2.tar.gz \
    && cd httrack-3.49.2 && ./configure && make && make install \
    && cd .. && rm -rf httrack-3.49.2*

# Set library path
ENV LD_LIBRARY_PATH="/usr/local/lib"

# Create working directory
WORKDIR /app

# Set the entry point for the Docker container
ENTRYPOINT ["python", "script/compress.py"]
