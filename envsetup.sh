#!/bin/bash

# Step 1: Create a virtual environment
echo "Creating a virtual environment named 'env'..."
python3 -m venv env

# Step 2: Activate the virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows environment
    echo "Activating virtual environment for Windows..."
    source env/Scripts/activate
else
    # Unix-based environment (Linux, macOS)
    echo "Activating virtual environment for Unix-based system..."
    source env/bin/activate
fi

# Check if virtual environment was activated
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment activated. Your terminal prompt should show (env)."
else
    echo "Failed to activate virtual environment."
    exit 1
fi

# Step 3: Upgrade pip and install Django
echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing Django..."
python -m pip install Django

# Confirm Django installation
echo "Django version installed:"
python -m django --version

echo "Setup complete. The virtual environment 'env' is now ready with Django installed."
echo "To reactivate later, use 'source env/bin/activate' on Unix or 'env\\Scripts\\activate' on Windows."
