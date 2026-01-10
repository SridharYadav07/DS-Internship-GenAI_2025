from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return "", 204

## Home route
@app.route("/", methods=["GET"])
def home():
    # Get the name from URL query parameter
    name = request.args.get("name")
    
    if name:
        name = name.upper()

    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)