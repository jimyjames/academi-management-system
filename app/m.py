from . import db 


class Students(db.Model):
    __tablename__ ="students"

#    creating the individual columns for the table 
    id=db.Column(db.Integer, primary_key=True)
    student_reg=db.Column(db.String(20), unique=True, nullable=False, index=True)
    fname=db.Column(db.String(16), nullable=False)
    mname=db.Column(db.String(16), nullable=False)
    sname=db.Column(db.String(16), nullable=False)
    username=db.Column(db.String(15), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    phone=db.Column(db.String(15), nullable=False)
    yoe = db.Column(db.String(10), nullable=False)
    password=db.Column(db.String(60), nullable=False)
    status=db.Column(db.String(20), nullable=False)
    department_id=db.Column(db.Integer, db.ForeignKey(departments.id), nullable=False)


    enrolled_student=db.relationship('Enrollments', backref=bdb.backref('student_id'), lazy=True)

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
         "department_id":departments.id
         }
        return json_student
    



    # creating the table fr units
class Units(db.Model):
    __tablename__="Units"

    # defining columns for the units table 
    id=db.Column(db.Integer,primary_key=True)
    code=db.Column(db.String(10), unique=True, index=True, nullable=False)
    name=db.Column(db.String(16), nullable=False)
    department_id = db.Column(db.String(16), db.ForeignKey('departments.id'), nullable=False)
    status=db.Column(db.String(20), nullable=False)
    Y_id=db.Column(db.Integer, db.Foreign('years.id',nullable=False))
    Lecturer_id=db.Columb(db.Foreign('Lecturers.id'),nullable=False)



    #  defining relatioships 
    enrollments=db.relationship('Enrollment', backref='unit_id', lazy=True)
    # course_id = db.relationship('Marks', backref=db.backref('courses_id', lazy=True))
   
   
    def to_json(self):
        json_unit = {
            "name":self.name,
            "id":self.id,
            "code":self.code,
            "email":self.email,
            "status":self.status,
            "department_id":self.department
            }
        
        return json_unit    
    


    # creating a table for enrollments
    # Note that the enrollments table is a junction table between the Units table and the units table 
    class Enrollments(db.Model):
        __tablename_="enrollments"
        
            # defining columns for the junction table enrollments
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
        course_id = db.Column(db.Integer, db.ForeignKey('units.code'))

        student_mark_enrolled=db.relationship('Marks', backref=db.backref('enrolled_id'), lazy= True)


        def to_json(self):
            json_enrollment = {
                "id":self.id,
                "student": self.student_id,
                "course": self.course_id
            
             }

            return json_enrollment
    

class Departments(db.Model):
    __tablename__="departments"


    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(50), nullable=False, unique=True)
    code=db.Column(db.String(10), unique=True, nullable=False)
    email=db.Column(db.String(50), nullable=False)
    phone=db.Column(db.String(12), nullable=False)

    Lecture_dept=db.relationship('Lectures', backref=db.backref('department_id', lazy=True))
    Student_dept=db.relationship('Students', backref=db.backref('department_id', lazy=True))
    


    def to_json(self):
        json_departments = {
            "id":self.id,
            "name":self.name,
            "code":self.code,
            "email":self.email,
            "phone":self.phone
            }
        return json_departments



class Modules(db.Model):
    __tablename__="modules"


    id=db.Column(db.Integer, primary_key=True, nullable=False)
    name=db.Column(db.String(10), nullable=False)
    semester=db.Column(db.Integer, nullabe=False)
    year=db.Column(db.Integer, nullable=False)
    code=db.Column(db.Integer, nullable=False, unique=True)

    unit_time=db.relationship('Units', backref=db.backref('Module_id'), lazy=True)

    def to_json(self):
        json_modules={
            "id":self.id,
            "name":self.name,
            "code":self.code,
            "semester":self.semester,
            "year":self.year
        }
        return json_modules
    

class Lecturers(db.Model):
    __tablename__="lecturers"

    id=db.Column(db.Integer, primary_key=True, nullable=False)
    fname=db.Column(db.String(20), nullable=False)    
    mname=db.Column(db.String(20), nullable=False)
    sname=db.Column(db.String(20), nullable=False)
    username=db.Column(db.String(30), nullble=False, unique=True)
    department_id=db.Column(db.Integer, db.ForeignKey('departments.id', nullable =False))
    email=db.Column(db.String(50), unique=True, nullable=True)
    code=db.Column(db.Integer, unique=True, nullable=True)
    phone=db.Column(db.String(12), unique=True, nullable=True)


    unit_lecturer=db.relationship('Units', backref=db.backref('lecturer_id'), lazy=True)



    def to_json(self):
        json_lecturers={
            "id":self.id,
            "fname":self.fname,
            "mname":self.mname,
            "sname":self.sname,
            "username":self.username,
            "department_id":self.department_id,
            "email":self.email,
            "code":self.code,
            "phone":self.phone
        }
        return json_lecturers
    


class Marks(db.Model):
    __tablename__="marks"
    
    id=db.Column(db.Integer,primary_key=True)
    enrollment_id=db.Column(db.Integer, db.ForeignKey('enrollments.id'),nullable=False)
    cat1=db.Column(db.Float(),nullable=False)
    Cat2=db.Column(db.Float(),nullable=False)
    cat3=db.Column(db.Float(),nullable=False)
    assignment1=db.Column(db.Float(),nullable=False)
    assignment2=db.Column(db.Float(),nullable=False)
    assignment3=db.Column(db.Float(),nullable=False)
    practicals=db.Column(db.Float(),nullable=False)
    mainExam=db.Column(db.Float(),nullable=False)
    overallmarks=db.Column(db.Float(),nullable=False)

    result=db.relationship('Results', backref=db.backref('mark_id'), lazy=True)

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
    mark_id = db.Column(db.Integer, db.ForeignKey('enrollments.id'), nullable=False)
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
         "mark_id":self.mark_id
         }
        
        return json_result



