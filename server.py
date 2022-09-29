from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<colorOne>/<colorTwo>')
def renderCheckerboard(x=8,y=8, colorOne="red", colorTwo="black"):
    return render_template('index.html', x=x, y=y, colorOne = colorOne, colorTwo = colorTwo)


if __name__ == "__main__":
    app.run(debug=True)