# Import the Flask module
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and its handler function
@app.route('/')
def hello_world():
    return 'Welcome.. I am a sample app!'

# Run the application
if __name__ == '__main__':
    app.run()
