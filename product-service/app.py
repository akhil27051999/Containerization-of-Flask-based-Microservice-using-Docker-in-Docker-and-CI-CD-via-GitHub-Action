# Import the Flask class from the flask package
from flask import Flask

# Create an instance of the Flask application
# '__name__' helps Flask locate resources and set the application context
app = Flask(__name__)

# Define a route for the root URL ('/')
# When someone accesses http://<host>:<port>/, this function will be triggered
@app.route('/')
def home():
    # This is the response that will be sent to the browser
    return "Product Service is running!"

# This block ensures the application runs only if this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server
    # host='0.0.0.0' makes the service accessible from outside the container or host
    # port=5002 specifies the port number on which this service will run
    app.run(host='0.0.0.0', port=5002)
