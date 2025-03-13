"""
Test script to verify that app_server.py works correctly.
"""

try:
    from app_server import app
    print("Successfully imported app from app_server.py")
    print(f"App type: {type(app)}")
    print("App should be callable for Gunicorn")
except Exception as e:
    print(f"Error importing app from app_server.py: {e}") 