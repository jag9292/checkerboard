from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", vertical = 8, horizontal = 8)

@app.route('/<x>')
def varx(x):
    return render_template("index.html", horizontal = 8, vertical = int(x))

@app.route('/<x>/<y>')
def varxy(x, y):
    return render_template("index.html", horizontal = int(y), vertical = int(x))

if __name__=="__main__":  
    app.run(debug=True)