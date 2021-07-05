# Using Python Flask to interact with a browser

# Install flask using pip and import it
from flask import Flask, redirect, url_for, render_template

# We have to create an object of this class
app = Flask(__name__)  # Creating an app instance


# Function to link to the default/home page
# Connect function to browser
@app.route("/")  # Decorating our function with @app.route to set the route in our browser
def index():
    return "Welcome to Engineering 89 DevOps team." \
           "<h3> <a href='/welcome'>Welcome</a> </h3>"\
           "<h3> <a href='/login'>Login</a> </h3>"

# "flask run" in terminal to run flask


# Creating welcome page
@app.route("/welcome/")  # You should always put the second forward slash so that it works even if you don't write it
# on the browser
def welcome():
    # return "<h1> Welcome page for Flask app </h1>"
    return render_template("welcome.html")  # Use .html file we created


# Create a decorator to route traffic to login page
# Display 2 messages of your choice in form of h1 and h2

# What if login page is unavailable?
# Redirect users if they visit login page
@app.route("/login/")
def login():  # Redirect and url_for we need to import in order to redirect users
    # return "<h1> Welcome to Login page</h1>" \
    #        "<h2> Login: </h2>"
    return redirect(url_for("welcome"))  # This redirects the user to welcome page


if __name__ == "__main__":
    app.run(debug=True)

# Add HTML file to redirect from Python flask to .html file
# We need to create a folder called "templates"
# project folder
    # >templates folder
        # >welcome.html
    # >app.py

