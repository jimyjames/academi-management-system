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
    # department = db.Column(db.String(16), db.ForeignKey('departments.name'), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    status=db.Column(db.String(20), nullable=False)


    enrollments1=db.relationship('Enrollment', backref='studentreg', lazy=True)
    # student_marks = db.relationship('Marks', backref=db.backref('reg', lazy=True))
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
         "student_reg":self.student_reg
        #  "dept":self.department
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



# class Departments(db.Model):
#     __tablename__= "departments"

#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(16), nullable=False)
#     email=db.Column(db.String(120), unique=True, nullable=False)
#     phone=db.Column(db.String(15), nullable=False)
#     code=db.Column(db.String(10), unique=True, nullable=False, index=False)
#     learners=db.relationship('Students', backref=db.backref('reg',lazy=True))
#     courses=db.relationship('Units',backref=db.backref('course_id',lazy=True) )
#     # image_fie=db.Column(db.String(20), nullable=False, default='default.jpg') 
#     def to_json(self):
#         json_department = {
#          "name":self.name,
#          "email":self.email,
#          "phone":self.phone,
#          "code":self.code
         
#          }
        
#         return json_department



    

# # class Lecturers(db.Model):
# #     id=db.Column(db.Integer,primary_key=True)
# #     fname=db.Column(db.String(16), nullable=False)
# #     mname=db.Column(db.String(16), nullable=False)
# #     sname=db.Column(db.String(16), nullable=False)
# #     email=db.Column(db.String(120), unique=True, nullable=False)
# #     phone=db.Column(db.String(15), nullable=False)
# #     image_fie=db.Column(db.String(20), nullable=False, default='default.jpg')
# #     password=db.Column(db.String(60), nullable=False)
# #     status=db.Column(db.String(20), nullable=False)

class Units(db.Model):
    __tablename__= "units"

    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(10), unique=True, index=True, nullable=False)
    
    name=db.Column(db.String(16), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    # department = db.Column(db.String(16), db.ForeignKey('departments.code'), nullable=False)
    enrollments=db.relationship('Enrollment', backref='unit_id', lazy=True)
    status=db.Column(db.String(20), nullable=False)
    def to_json(self):
        json_unit = {
         "name":self.name,
         "id":self.id,
         "code":self.code,
         "email":self.email,
         "status":self.status
        #  "department":self.department
         }
        
        return json_unit


class Enrollment(db.Model):
    __tablename__="enrollment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('units.code'))
    # enrollment_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Define relationships to access related data
    student = db.relationship('Students', backref=db.backref('enrollments', lazy=True))
    # course = db.relationship('Units', backref=db.backref('enrollments', lazy=True))

    def to_json(self):
        json_enrollment = {
            "id":self.id,
            "student": self.student_id,
            "course": self.course_id
            # "enroll_date": self.enrollment_date
        }

        return json_enrollment

  


# class Years(db.Model):
#     __tablename__= "year"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10))
#     year = db.Column(db.Integer)
#     semester = db.Column(db.Integer)


#     def to_json(self):
#         json_years={
#             "name":self.name,
#             "year":self.year,
#             "semester":self.semester
#         }



           
# class Marks(db.Model):
#     __tablename__= "marks"

#     id=db.Column(db.Integer,primary_key=True)
#     reg = db.Column(db.Integer, db.ForeignKey('students.reg'), nullable=False)
#     course_id = db.Column(db.Integer, db.ForeignKey('units.code'), nullable=False)
#     cat1=db.Column(db.Float(),nullable=False)
#     Cat2=db.Column(db.Float(),nullable=False)
#     cat3=db.Column(db.Float(),nullable=False)
#     assignment1=db.Column(db.Float(),nullable=False)
#     assignment2=db.Column(db.Float(),nullable=False)
#     assignment3=db.Column(db.Float(),nullable=False)
#     practicals=db.Column(db.Float(),nullable=False)
#     mainExam=db.Column(db.Float(),nullable=False)
#     overallmarks=db.Column(db.Float(),nullable=False)

#     reg = db.relationship('Students', backref=db.backref('reg', lazy=True))
#     course = db.relationship('Units', backref=db.backref('course_id', lazy=True))

#     def to_json(self):
#         json_mark = {
            
#          "cat1":self.cat1,
#          "Cat2":self.Cat2,
#          "cat3":self.cat3,
#          "assignment1":self.assignment1,
#          "assignment2":self.assignment2,
#          "assignment3":self.assignment3,
#          "practicals":self.practicals,
#          "mainExam":self.mainExam,
#          "overallmarks":self.overallmarks,
#          "reg":self.reg,
#          "course_id":self.course_id}
        
#         return json_mark

# class Results(db.Model):
#     __tablename__= "results"
#     id=db.Column(db.Integer,primary_key=True)
#     reg = db.Column(db.Integer, db.ForeignKey('students.reg'), nullable=False)
#     course_id = db.Column(db.Integer, db.ForeignKey('units.code'), nullable=False)

#     firstattempt=db.Column(db.Float(),nullable=False)
#     secondattempt=db.Column(db.Float(),nullable=False)
#     thirdattempt=db.Column(db.Float(),nullable=False)
#     finalattempt=db.Column(db.Float(),nullable=False)
#     reg = db.relationship('Students', backref=db.backref('marks', lazy=True))
#     course = db.relationship('Units', backref=db.backref('marks', lazy=True))

#     def to_json(self):
#         json_result = {
#          "firstattempt":self.firstattempt,
#          "secondattempt":self.secondattempt,
#          "thirdattempt":self.thirdattempt,
#          "finalattempt":self.finalattempt,
#          "course":self.course_id,
#          "student":self.reg
#          }
        
#         return json_result

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


