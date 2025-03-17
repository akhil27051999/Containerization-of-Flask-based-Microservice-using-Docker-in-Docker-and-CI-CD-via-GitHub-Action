# Import the Flask class from the flask package
from flask import Flask

# Create a Flask application instance
# '__name__' helps Flask determine the root path of the application
app = Flask(__name__)

# Define a route for the root URL ('/') of the web application
# When someone visits http://<host>:<port>/, this function will run
@app.route('/')
def home():
    # This is the response that will be shown in the browser
    return "Order Service is running!"

# This ensures the app runs only when the script is executed directly,
# not when it's imported as a module in another file
if __name__ == '__main__':
    # Start the Flask web server
    # host='0.0.0.0' means it will be accessible from any IP (inside Docker too)
    # port=5003 specifies the port number for the service
    app.run(host='0.0.0.0', port=5003)
    
# Quick Explanation:
# Flask(__name__) initializes the app.
# @app.route('/') is used to map the URL / to the home() function.
# app.run() starts the development server
