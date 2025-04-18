#!/bin/bash
echo "Setting up WebWordGen..."
# Install Python and pip
if [[ "$OSTYPE" == "linux-android"* ]]; then
    pkg update && pkg upgrade
    pkg install python
else
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi
pip3 install -r requirements.txt
mkdir -p output
echo "Setup complete! Run: python3 webwordgen.py"
