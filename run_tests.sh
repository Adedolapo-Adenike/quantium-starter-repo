#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the test suite
pytest test_app.py

# Capture pytest's exit code and use it as this script's exit code
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi