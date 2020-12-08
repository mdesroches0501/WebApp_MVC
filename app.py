# app.py - entry point for application

from flask import Flask
from models import Course
from models import CourseView
from service import CourseController

app = Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

@app.route("/MVS")
def main():
    returnString = ''
    returnString = returnString + ("Welcome to your courses...")
    course = Course("Design Patterns","CS330","A fun class for you to learn")

    courseView = CourseView()
    courseController = CourseController(course, courseView)
    returnString = returnString + courseController.updateView()

    courseController.setCourseDescription("It will teach you to do thing like this")
    returnString = returnString + courseController.updateView()
    return returnString

def updateView(self):
    return str(self.model.getName()+ self.model.getNumber()+ self.model.getDescription())

if __name__ == "__main__":
    main()
    app.run(debug=True)
