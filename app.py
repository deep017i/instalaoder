#The repo is fully coded and modified by @Dypixx.
#Please do not sell or remove credits.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Dypixx'


if __name__ == "__main__":
    app.run()
