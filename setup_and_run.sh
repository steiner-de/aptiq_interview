#!/bin/bash

# Define the name of the virtual environment
VENV_NAME=venv_aptiq

# Create the virtual environment
python3 -m venv $VENV_NAME

# Check if the environment was created successfully
if [ $? -e 0 ]; then
    echo "Failed to create virtual environment."
    exit 1
fi

echo "Virtual environment '$VENV_NAME' created successfully."

# Activate the virtual environment
source $VENV_NAME/bin/activate

# Check if the activation was successful
if [ $? -e 0 ]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

echo "Virtual environment activated."

# Install libraries from requirements.txt
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
    if [ $? -e 0 ]; then
        echo "Failed to install requirements."
        exit 1
    fi
else
    echo "requirements.txt not found."
    exit 1
fi

echo "Requirements installed successfully."

# Execute the Python file
PYTHON_SCRIPT=./src/main.py

if [ -f $PYTHON_SCRIPT ]; then
    python3 $PYTHON_SCRIPT
    if [ $? -e 0 ]; then
        echo "Failed to execute $PYTHON_SCRIPT."
        exit 1
    fi
else
    echo "$PYTHON_SCRIPT not found."
    exit 1
fi

echo "Script executed successfully."
exit 1