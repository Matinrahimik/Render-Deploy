"""
This file serves as an explicit entry point for Gunicorn.
It imports the server from app.py and exposes it as 'app'.
"""

from app import server as app

# This is the variable that Gunicorn looks for
# The name 'app' is what Gunicorn expects by default

if __name__ == "__main__":
    app.run() 