from flask import Flask

helloworld = Flask(__name__)

@helloworld.route("/")
def home():
    return "{\"message\": \"hey python\"}"

@helloworld.route("/home")
def homepage():
    return "{\"this is home page\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=3000, debug=True)
