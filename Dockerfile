FROM nvcr.io/nvidia/tensorflow:25.02-tf2-py3

# Install system dependencies OpenCV needs
RUN apt-get update && apt-get install -y \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Force NumPy <2.0 and install Python libs
RUN pip install --upgrade "numpy<2.0" \
    opencv-python \
    matplotlib \
    mediapipe 

WORKDIR /workspace
