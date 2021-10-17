import os
from flask import Flask
# since the env.py file is not pushed to GitHub, this finds the file locally
if os.path.exists("env.py"):
    import env


# this creates an instance of flask and stored in a variable
app = Flask(__name__)


# the / refers to the default route
@app.route("/")
def hello():
    return "Cycle Motion"


# this tells our app how and where to run our application
if __name__ == "__main__":
    # this fetches the default value from env.py file
    app.run(host=os.environ.get("IP"),
            # converts the port into an integer
            port=int(os.environ.get("PORT")),
            # prior to actual deployment, update this to debug=False
            debug=True)