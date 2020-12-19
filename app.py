from flask import Flask, render_template, request
#I have no idea what i'm doing
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def print_groups():
    names = request.form['names']
    return names


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)