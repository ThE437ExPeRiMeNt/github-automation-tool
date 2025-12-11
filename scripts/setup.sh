#!/bin/bash

# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip -y

# Install required Python packages
pip3 install -r requirements.txt

echo "Setup complete!"
