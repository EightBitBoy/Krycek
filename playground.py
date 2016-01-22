from flask import Flask, g

app = Flask(__name__)

@app.route("/")
def index():
	return "index"


@app.route("/status")
def status():
	return "status"


def consume():
	return "consume"

if __name__ == "__main__":
	app.debug = True
	app.run()
