import sqlite3
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__) 

conn = sqlite3.connect('database.db')
c = conn.cursor()
print("Opened database successfully")

#create users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
userID VARCHAR(100) NOT NULL PRIMARY KEY,
firstName VARCHAR(50),
lastName VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
fieldOfEngineering VARCHAR(50) NOT NULL, 
skillLevel INT NOT NULL,
timeAvailable INT NOT NULL,
password CHAR(8) NOT NULL);''')
conn.commit()
conn.close()
print("User table created successfully")

#create projects table
conn = sqlite3.connect('database.sqlite')
conn.execute('''CREATE TABLE IF NOT EXISTS projects (
projectID VARCHAR(100) NOT NULL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
category VARCHAR(50) NOT NULL,
description VARCHAR(500) NOT NULL,
skillLevel INT NOT NULL,
timeNeeded INT NOT NULL,
numOfFavourites INT NOT NULL,);''')
conn.commit()
conn.close()
print( "Project table created successfully")


#user class 
class User:
    def __init__(self, userID, firstName, lastName, email, fieldOfEngineering, skillLevel, timeAvailable, password):
      self.userID = userID
      self.firstName = firstName
      self.fastName = lastName
      self.email = email
      self.fieldOfEngineering = fieldOfEngineering
      self.skillLevel = skillLevel
      self.TimeAvailable = timeAvailable
      self.password = password

    #create an user object
    def CreateUser(self, userID, FirstName, LastName, Email, Field_of_engineering, skill_level, time_available, password):
      user = User(userID, FirstName, LastName, Email, Field_of_engineering, skill_level, time_available, password)

    #get recommended projects for specific user
    def GetRecommendedProjects(self):
      conn = sqlite3.connect('database.sqlite')
      c = conn.cursor()
      project = c.execute(f'''
      SELECT * FROM projects WHERE FieldOfEngineering = {self.FieldOfEngieering} AND SkillLevel = {self.SkillLevel} AND TimeAvailable = {self.TimeAvailable}''');
      conn.commit()
      conn.close()
      return project


@app.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        fieldOfEngineering = request.form['fieldOfEngineering']
        skillLevel = request.form['skillLevel']
        timeAvailable = request.form['timeAvailable']
        password = request.form['password']
      
        conn = sqlite3.connect('database.sqlite')
        #conn.execute(f'''INSERT INTO users (firstName, lastName, email, fieldOfEngineering, skillLevel, timeAvailable, password) VALUES ('{firstName}', '{'{email}', '{password}')''')
        #conn.commit
        CreateUser()

        conn = sqlite3.connect('database.sqlite')
        conn.execute(f'''INSERT INTO projects (title, category, description, skill_level, time_needed, num_of_favourites) VALUES ('p1', 'p2', 'p3', 'p4', 'p5', 'p6')''')
        
        
      
    return render_template("login.html") 

@app.route('/signup', methods=['GET', 'POST']) 
def signup():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    print(email)
    print(password)


# running application 
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0') 