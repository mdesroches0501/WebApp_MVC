# models.py - handles everything that involves a Database
import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('toDo.db')
        self.createUserTable()
        self.createToDoTable()
    
    def createToDoTable(self):

        query = """
        CREATE TABLE IF NOT EXISTS "ToDo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def createUserTable(self):

        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        );
        """

        self.conn.execute(query)

# This is the model of the MVC
class Course:
    def __init__(self, _name, _number, _description):           # constructor for Course class
        self.name = _name
        self.number = _number
        self.description = _description
    
    def getName(self):
        return self.name
    def getNumber(self):
        return self.number
    def getDescription(self):
        return self.description
    # Set the name to the string n
    def setName(self,n):
        self.name = n
    # Set the number to the string n   
    def setNumber(self,n):
        self.number = n
    # Set the description to the string d
    def setDescription(self,d):
        self.description = d

#This is the view in the MVC
class CourseView:
    def __init__(self):
        pass
    def printCourseDetails(self,courseName,courseNumber,courseDescription):
        return str("Course: " + courseName 
                + "Number: " + courseNumber 
                + "Description: " + courseDescription)
