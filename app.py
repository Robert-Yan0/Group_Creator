from flask import Flask, render_template, request
#I have no idea what i'm doing
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

def parseGroup(groupNames, groupNumber, groupPeople):
    finalGroup = "Names:\n" + groupNames + "\n" + "Number of Groups:\n" + groupNumber + "\n" + "Number of people in a group:\n" + groupPeople
    return finalGroup

@app.route('/', methods=['POST'])
def printNames():
    names = request.form['names']
    numOfGroups = request.form['numOfGroups']
    peoplePerGroup = request.form['peoplePerGroup']
    return parseGroup(names, numOfGroups, peoplePerGroup)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)