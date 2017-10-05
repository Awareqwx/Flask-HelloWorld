import flask

app = flask.Flask(__name__)

@app.route("/")
def helloWorld():
    return flask.render_template("world.html")
app.run(debug=True)