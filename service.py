# service.py - converts the request into a response

from models import Course
from models import CourseView

# This is the controller in MVC

# Model and view are required to be instantiated before this class.

#inherits from model and view
class CourseController():

    def __init__(self, _model, _view):
        self.model = Course(_model.getName(), _model.getNumber(), _model.getDescription()) 
        self.view = CourseView()

    def setCourseName(self, name):
        self.model.setName(name)
  
    def getCourseName(self): 
        return self.model.getName() 

    def setCourseNumber(self,courseNo):
        self.model.setNumber(courseNo)

    def getCourseNumber(self):
        return self.model.getNumber()
  
    def setCourseDescription(self, description):
        self.model.setDescription(description)

    def getCourseDescription(self):
        return self.model.getDescription()

    def updateView(self):
        return str(self.model.getName()+ self.model.getNumber()+ self.model.getDescription())


