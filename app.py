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
    returnString = returnString + ("Welcome to your courses...\n")
    course = Course("Design Patterns\n","CS330\n","A fun class for you to learn\n")

    courseView = CourseView()
    courseController = CourseController(course, courseView)
    returnString = returnString + str(courseController.updateView())

    courseController.setCourseDescription("It will teach you to do thing like this")
    returnString = returnString + str(courseController.updateView())

    return returnString

if __name__ == "__main__":
    main()
    app.run(debug=True)
