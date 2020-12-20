from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

#This is a version of the code where I have not included group sorting yet
#The code commented out is the code that is supposed to sort the groups but doesn't work


#def createGroup(groupNames,groupPeople,groupsNumber):          #GroupsNumber is the number of group already created, not the number of groups in total
#    namesOfGroup = namesOfGroup + "Group " + str(groupsNumber) + "\n"      
#    for i in groupNames:
#        if i == groupPeople: #group people is the number of people per group
#            break
#        namesOfGroup += groupNames[i]
#        groupNames.remove(i)

#    return namesOfGroup
        

def parseGroup(groupNames, groupNumber, groupPeople):
    return "Names:\n" + groupNames + "\n" + "Number of groups:\n" + groupNumber + "\n" + "Number of people in a group: \n" + groupPeople
#    numberOfGroups = 0
#    groupNameList = groupNames.split()
#    finalGroup = ""
#    numOfNames = len(groupNameList)
#    if numOfNames < (groupNumber * groupPeople):
#        return "Error, number of groups or number of people too large"
#
#    while numberOfGroups < groupNumber:
#        numberOfGroups += 1
#        finalGroup += createGroup(groupNameList,groupPeople,groupsNumber)
#    return finalGroup

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