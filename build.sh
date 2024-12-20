#!/bin/bash

# Build the main.py script into an executable using Nuitka

# Ensure the script exits if any command fails
set -e

# 激活虚拟环境
source .venv/bin/activate

# Run the Nuitka command to compile main.py into an executable
nuitka \
--standalone \
--onefile \
--output-dir=dist \
--remove-output \
main.py

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Build successful. The executable is located in the 'dist' directory."
else
    echo "Build failed."
    exit 1
fi
