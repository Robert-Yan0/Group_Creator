from flask import Flask, render_template, request
#I have no idea what i'm doing
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

def createObject(groupNames,groupPeople,groupsNumber):
    numberOfGroups = str(groupsNumber)          #GroupsNumber is the number of group already created, not the number of groups in total
    namesOfGroup += "Group " + numberOfGroups + "\n"      
    for i in groupNames:
        if i == groupPeople: #group people is the number of people per group
            break
        namesOfGroup += groupNames[i]
        groupNames.remove(i)

    return namesOfGroup
        

def parseGroup(groupNames, groupNumber, groupPeople):
    groupsNumber = 0
    groupNameList = groupNames.split()
    finalGroup = ""
    if len(groupNameList) < (groupNumber * groupPeople):
        return "Error, number of groups or number of people too large"
    while numOfGroups != groupNumber:
        groupsNumber += 1
        finalGroup += createObject(groupNameList,groupPeople,groupsNumber)
    #finalGroup = "Names:" + groupNames + "Number of Groups:" + groupNumber + "Number of people in a group:" + groupPeople
    #return finalGroup

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