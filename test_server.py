"""
Test script to verify that the server can be imported correctly.
This helps diagnose deployment issues.
"""

try:
    from app import server
    print("Successfully imported server from app.py")
    print(f"Server type: {type(server)}")
    print("Server should be callable for Gunicorn")
except Exception as e:
    print(f"Error importing server: {e}")
    
try:
    from wsgi import server
    print("Successfully imported server from wsgi.py")
    print(f"Server type: {type(server)}")
    print("Server should be callable for Gunicorn")
except Exception as e:
    print(f"Error importing server from wsgi.py: {e}") 