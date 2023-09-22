from flask_sqlalchemy import SQLAlchemy
from . import db
class Students(db.Model):
    __tablename__= "students"

    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(16), nullable=False)
    mname=db.Column(db.String(16), nullable=False)
    sname=db.Column(db.String(16), nullable=False)
    # username=db.Column(db.String(15), unique=True, nullable=False)
    # email=db.Column(db.String(120), unique=True, nullable=False)
    # phone=db.Column(db.String(15), nullable=False)
    # yoe=db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    # image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    status=db.Column(db.String(20), nullable=False)

    def to_json(self):
        json_student = {
         "fname":self.fname,
         "mname":self.mname,
         "sname":self.sname,
         "password":self.password,
         "status":self.status}
        
        return json_student





# class Schools(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(16), nullable=False)
#     email=db.Column(db.String(120), unique=True, nullable=False)
#     phone=db.Column(db.String(15), nullable=False)
#     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
    

# class Courses(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(16), nullable=False)
#     # email=db.Column(db.String(120), unique=True, nullable=False)
#     phone=db.Column(db.String(15), nullable=False)
#     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')



class Departments(db.Model):
    __tablename__= "departments"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    # image_fie=db.Column(db.String(20), nullable=False, default='default.jpg') 
    def to_json(self):
        json_department = {
         "name":self.name,
         "email":self.email,
         "phone":self.phone,
         }
        
        return json_department



    

# class Lecturers(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     fname=db.Column(db.String(16), nullable=False)
#     mname=db.Column(db.String(16), nullable=False)
#     sname=db.Column(db.String(16), nullable=False)
#     email=db.Column(db.String(120), unique=True, nullable=False)
#     phone=db.Column(db.String(15), nullable=False)
#     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
#     password=db.Column(db.String(60), nullable=False)
#     status=db.Column(db.String(20), nullable=False)

class Units(db.Model):
    __tablename__= "units"

    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(10), unique=True, nullable=False)
    name=db.Column(db.String(16), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    # image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
    status=db.Column(db.String(20), nullable=False)
    def to_json(self):
        json_unit = {
         "name":self.name,
         "code":self.code,
         "email":self.email,
         "status":self.status
         }
        
        return json_unit


class Marks(db.Model):
    __tablename__= "marks"

    id=db.Column(db.Integer,primary_key=True)
    cat1=db.Column(db.Float(),nullable=False)
    Cat2=db.Column(db.Float(),nullable=False)
    cat3=db.Column(db.Float(),nullable=False)
    assignment1=db.Column(db.Float(),nullable=False)
    assignment2=db.Column(db.Float(),nullable=False)
    assignment3=db.Column(db.Float(),nullable=False)
    practicals=db.Column(db.Float(),nullable=False)
    mainExam=db.Column(db.Float(),nullable=False)
    overallmarks=db.Column(db.Float(),nullable=False)
    def to_json(self):
        json_mark = {
         "cat1":self.cat1,
         "Cat2":self.Cat2,
         "cat3":self.cat3,
         "assignment1":self.assignment1,
         "assignment2":self.assignment2,
         "assignment3":self.assignment3,
         "practicals":self.practicals,
         "mainExam":self.mainExam,
         "overallmarks":self.overallmarks}
        
        return json_mark


class Results(db.Model):
    __tablename__= "results"

    id=db.Column(db.Integer,primary_key=True)
    firstattempt=db.Column(db.Float(),nullable=False)
    secondattempt=db.Column(db.Float(),nullable=False)
    thirdattempt=db.Column(db.Float(),nullable=False)
    finalattempt=db.Column(db.Float(),nullable=False)
    def to_json(self):
        json_result = {
         "firstattempt":self.firstattempt,
         "secondattempt":self.secondattempt,
         "thirdattempt":self.thirdattempt,
         "finalattempt":self.finalattempt,
         }
        
        return json_result

# class Users(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     fname=db.Column(db.String(16), nullable=False)
#     mname=db.Column(db.String(16), nullable=False)
#     sname=db.Column(db.String(16), nullable=False)
#     email=db.Column(db.String(120), unique=True, nullable=False)
#     phone=db.Column(db.String(15), nullable=False)
#     yoe=db.Column(db.datetime(), nullable=False)
#     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
#     password=db.Column(db.String(60), nullable=False)
#     status=db.Column(db.String(20), nullable=False)


