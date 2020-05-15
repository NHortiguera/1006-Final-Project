#######################
# Name: Nicolas Hortiguera
# Uni: nh2648
# Assignment: Final
# 
# This module contains functions to run a server on the local host using Flask.
#######################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

#route to classes page
@app.route("/classes")
def classes():
    return render_template("classes.html")

#route to assignments page
@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

#start the server
if __name__ == "__main__":
    app.run()