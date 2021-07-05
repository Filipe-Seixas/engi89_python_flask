# Using Python Flask to interact with a browser

# Install flask using pip and import it
from flask import Flask

# We have to create an object of this class
app = Flask(__name__)  # Creating an app instance


# Function to link to the default/home page
# Connect function to browser
@app.route("/")  # Decorating our function with @app.route to set the route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team."

# "flask run" in terminal to run flask


# Creating welcome page
@app.route("/welcome/")  # You should always put the second forward slash so that it works even if you don't write it
# on the browser
def welcome():
    return "<h1> Welcome page for Flask app </h1>"


# Create a decorator to route traffic to login page
# Display 2 messages of your choice in form of h1 and h2

@app.route("/login/")
def login():
    return "<h1> Welcome to Login page</h1>" \
           "<h2> Login: </h2>"
