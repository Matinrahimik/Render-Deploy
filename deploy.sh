#!/bin/bash

# This script helps prepare and deploy the application to Render

echo "Preparing files for Render deployment..."

# Check if render-cli is installed
if ! command -v render &> /dev/null
then
    echo "render-cli not found. You can deploy manually by following the instructions in README.md"
    echo "Or install render-cli: npm install -g @render/cli"
else
    echo "render-cli found. You can deploy using: render deploy"
fi

# Verify that the simple Flask app works
echo "Testing simple Flask app..."
if python3 -c "from simple_app import app; print('Simple Flask app is working!')" 2>/dev/null; then
    echo "Simple Flask app is working correctly!"
else
    echo "Warning: Could not import simple_app. Make sure Flask is installed."
    echo "Try running: pip install flask"
fi

# Check if gunicorn is installed
if ! python3 -c "import gunicorn" 2>/dev/null; then
    echo "Warning: gunicorn is not installed in your local environment."
    echo "This is fine for deployment, but if you want to test locally, run: pip install gunicorn"
fi

echo "Files are ready for deployment!"
echo "Follow the instructions in README.md to deploy your application to Render."
echo "Once deployed, you can share the URL with anyone to access your dashboard."
echo ""
echo "If you encounter issues with deployment, try the following:"
echo "1. Make sure your requirements.txt includes all necessary packages"
echo "2. Check that your Procfile and render.yaml are correctly configured"
echo "3. Verify that your app has a callable Flask/Dash server object"
echo "4. Try deploying the simple Flask app first (simple_app.py) before the main app" 