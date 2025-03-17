# Import the Flask class from the flask module
from flask import Flask

# Create a new instance of the Flask application
# '__name__' helps Flask know where to look for templates, static files, etc.
app = Flask(__name__)

# Define a route for the root URL ('/')
# When someone visits http://<host>:<port>/, this function will be called
@app.route('/')
def home():
    # Return a simple response/message to confirm the service is running
    return "User Service is running!"

# This condition ensures the app runs only when this script is executed directly,
# and not when it's imported as a module in another file
if __name__ == '__main__':
    # Start the Flask development server
    # host='0.0.0.0' makes the app accessible externally (e.g., from Docker or another device)
    # port=5001 means the app will run on port 5001
    app.run(host='0.0.0.0', port=5001)
