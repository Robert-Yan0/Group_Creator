from flask import Flask, render_template, request
#I have no idea what i'm doing
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
 
#def parseNames(groupNames):
#    #I will change this function later
#     groupNames = groupNames.split()
#     for x in groupNames:
#         processedNames = processedNames + groupNames[x] + '\n'
#     return processedNames

def parseGroup(groupNames, groupNumber, groupPeople):
    finalGroup = "Names:\n" + groupNames + "\n" + "Number of Groups:\n" + groupNumber + "\n" + "Number of people in a group:\n" + groupPeople
    return finalGroup

@app.route('/', methods=['POST'])
def printNames():
    names = request.form['names']
    numOfGroups = request.form['numOfGroups']
    peoplePerGroup = request.form['peoplePerGroup']
    return parseGroup(names, numOfGroups, peoplePerGroup)

#numOfGroups = request.form['numOfGroups']
#peoplePerGroup = reqeust.form['peoplePerGroup']

#@app.route('/', methods=['POST'])
#def printGroupsNum():
#    numOfGroups = request.form['numOfGroups']
#    return numOfGroups

#@app.route('/', methods=['POST'])
#def printPeoplePerGroup():
#    peoplePerGroup = request.form['peoplePerGroup']
#    return peoplePerGroup


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)