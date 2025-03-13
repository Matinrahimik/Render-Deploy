"""
A simple Flask app that can be used as a fallback if the Dash app doesn't work.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <title>Survey Dashboard</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Survey Dashboard</h1>
                <p>The main application is currently being configured. Please check back soon.</p>
                <p>If you're seeing this page, it means the server is running but the main Dash application is not yet properly configured.</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True) 