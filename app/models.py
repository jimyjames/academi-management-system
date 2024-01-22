from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime
class Students(db.Model):
    __tablename__= "students"

    id=db.Column(db.Integer, primary_key=True)
    student_reg=db.Column(db.String(20), unique=True, nullable=False, index=True)
    fname=db.Column(db.String(16), nullable=False)
    mname=db.Column(db.String(16), nullable=False)
    sname=db.Column(db.String(16), nullable=False)
    username=db.Column(db.String(15), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    yoe = db.Column(db.String(10), nullable=False, default=datetime.utcnow)
    # image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    department = db.Column(db.String(16), db.ForeignKey('departments.name'), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    status=db.Column(db.String(20), nullable=False)
    current_module = db.Column(db.Integer, db.ForeignKey('years.id'))


    enrollments=db.relationship('Enrollments', backref='students_id', lazy=True)
    # markstudent_id = db.relationship('Marks', backref=db.backref('learner_id', lazy=True))
   
    # student_marks = db.relationship('Marks', backref=db.backref('reg', lazy=T
    # rue))
    # course = db.relationship('Marks', backref=db.backref('course_id', lazy=True))

    def to_json(self):
        json_student = {

    
         "fname":self.fname,
         "id":self.id,
         "mname":self.mname,
         "sname":self.sname,
         "password":self.password,
         "status":self.status,
         "email":self.email,
         "yoe":self.yoe,
         "phone":self.phone,
         "username":self.username,
         "student_reg":self.student_reg,
         
         "dept":self.department,
         "current_module":self.current_module
         }
        
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
    code=db.Column(db.String(10), unique=True, nullable=False, index=False)
    learners=db.relationship('Students', backref=db.backref('DepartmentId',lazy=True))
    courses=db.relationship('Units',backref=db.backref('Department_id',lazy=True) )
    lecturers=db.relationship('Lecturers', backref=db.backref('deptId'), lazy=True)
    # image_fie=db.Column(db.String(20), nullable=False, default='default.jpg') 
    def to_json(self):
        json_department = {
         "name":self.name,
         "email":self.email,
         "phone":self.phone,
         "code":self.code,
         "id":self.id
         
         }
        
        return json_department



    

class Lecturers(db.Model):
    __tablename__="lecturers"


    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(16), nullable=False)
    mname=db.Column(db.String(16), nullable=False)
    sname=db.Column(db.String(16), nullable=False)
    uname=db.Column(db.String(20),nullable=False,unique=True)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    code=db.Column(db.String(4), nullable=False, unique=True)
    dept_id=db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)


    def to_son(self):
        json_departments = {
         "fname":self.fname,
         "id":self.id,
         "mname":self.mname,
         "sname":self.sname,
         "password":self.password,
         "email":self.email,
         "phone":self.phone,
         "username":self.username,
         "code":self.code,
         "dept_id":self.dept_id
        }
        return json_departments



class Units(db.Model):
    __tablename__= "units"


    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(10), unique=True, index=True, nullable=False)
    module=db.Column(db.Integer, db.ForeignKey('years.id'), nullable=False)
    name=db.Column(db.String(16), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    department = db.Column(db.String(16), db.ForeignKey('departments.code'), nullable=False)
    enrollmentes=db.relationship('Enrollments', backref='unit_id', lazy=True)
    # course_id = db.relationship('Marks', backref=db.backref('courses_id', lazy=True))
    status=db.Column(db.String(20), nullable=False)
    def to_json(self):
        json_unit = {
         "name":self.name,
         "id":self.id,
         "code":self.code,
         "email":self.email,
         "status":self.status,
         "department":self.department,
         "module":self.__module__

         }
        
        return json_unit


class Enrollments(db.Model):
    __tablename__="enrollments"
    # Avoid multiple primary_keys in tables
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('units.id'))
    # enrollment_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Define relationships to access related data
    # student = db.relationship('Students', backref=db.backref('enrollments', lazy=True))
    marks_enroll_id = db.relationship('Marks', backref=db.backref('enrollments_id', lazy=True))

    def to_json(self):
        json_enrollment = {
            "id":self.id,
            "student": self.student_id,
            "course": self.course_id
            # "enroll_date": self.enrollment_date
        }

        return json_enrollment

  


class Years(db.Model):
    __tablename__= "years"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    year = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    code = db.Column(db.Integer,unique=True,nullable=False)
    Modules=db.relationship('Units', backref=db.backref('module_id'),lazy=True)
    currentmodule=db.relationship('Students', backref=db.backref('current module'),lazy=True)
    


    def to_json(self):
        json_years={
            "name":self.name,
            "year":self.year,
            "semester":self.semester,
            "code":self.code
        }



           
class Marks(db.Model):
    __tablename__= "marks"

    id=db.Column(db.Integer,primary_key=True)
    enrollment_id=db.Column(db.Integer, db.ForeignKey('enrollments.id'), nullable=False)
    # student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    # course_id = db.Column(db.Integer, db.ForeignKey('units.id'), nullable=False)
    cat1=db.Column(db.Float(),nullable=False)
    Cat2=db.Column(db.Float(),nullable=False)
    cat3=db.Column(db.Float(),nullable=False)
    assignment1=db.Column(db.Float(),nullable=False)
    assignment2=db.Column(db.Float(),nullable=False)
    assignment3=db.Column(db.Float(),nullable=False)
    practicals=db.Column(db.Float(),nullable=False)
    mainExam=db.Column(db.Float(),nullable=False)
    overallmarks=db.Column(db.Float(),nullable=False)

    results_mark_id=db.relationship('Results', backref=db.backref('marks_id',), lazy=True)
    # passingmarks=db.relationship('Results', backref=db.backref('overall marks'),lazy=True)




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
         "overallmarks":self.overallmarks,
         "enrollment_id":self.enrollment_id
         }
        
        return json_mark

class Results(db.Model):
    __tablename__= "results"

    id=db.Column(db.Integer,primary_key=True)
    # reg = db.Column(db.Integer, db.ForeignKey('students.reg'), nullable=False)
    # course_id = db.Column(db.Integer, db.ForeignKey('units.code'), nullable=False)
    mark_id=db.Column(db.Integer, db.ForeignKey('marks.id'), nullable=False)
    firstattempt=db.Column(db.Float(),nullable=False)
    secondattempt=db.Column(db.Float())
    thirdattempt=db.Column(db.Float())
    finalattempt=db.Column(db.Float())
    # firstattempt = db.Column(db.Float(), db.ForeignKey('marks.overallmarks', ondelete="CASCADE"), nullable=True)

 

    def to_json(self):
        json_result = {
         "id":self.id,
         "firstattempt":self.firstattempt,
         "secondattempt":self.secondattempt,
         "thirdattempt":self.thirdattempt,
         "finalattempt":self.finalattempt,
         "mark_id":self.mark_id
         }
        
        return json_result

# # class Users(db.Model):
# #     id=db.Column(db.Integer,primary_key=True)
# #     fname=db.Column(db.String(16), nullable=False)
# #     mname=db.Column(db.String(16), nullable=False)
# #     sname=db.Column(db.String(16), nullable=False)
# #     email=db.Column(db.String(120), unique=True, nullable=False)
# #     phone=db.Column(db.String(15), nullable=False)
# #     yoe=db.Column(db.datetime(), nullable=False)
# #     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
# #     password=db.Column(db.String(60), nullable=False)
# #     status=db.Column(db.String(20), nullable=False)


