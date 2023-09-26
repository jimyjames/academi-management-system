from . import ams
from flask import request,jsonify,render_template, url_for, redirect
from .. import db
from ..models import Students,Units,Enrollment,Marks
# ,Results
# ,Departments
from .forms import MarksForm,EnrollmentForm

@ams.route("/")
@ams.route("/home")
def home():
    return "<a href='/students'>View Students</a>"+ "<br>" + "<a href='/enrollments'>View Enrolled Students</a>"+ "<br>"+ "<a href='/newenrollments'>Enroll Students</a>" +"<br>" + "<a href='/marks'>View Marks </a>"+"<br>" + "<a href='/newmarks'>Add Marks</a>" + "<br>" +"<a href='/students'>View Students</a>"

@ams.route("/students",methods=["GET","POST"])
def students():
    if request.method=="GET":
        all_students = Students.query.all()
        student_list = []
        for student in all_students:
            student_list.append(student.to_json())
        return jsonify(student_list)
    
    if request.method=="POST":
        new_student=Students(
           
            fname=request.form["fname"],
            mname=request.form["mname"],
            sname=request.form["sname"],
            password=request.form["password"],
            status=request.form["status"],
            email=request.form["email"],
            yoe=request.form["yoe"],
            phone=request.form["phone"],
            username=request.form["username"],
            student_reg=request.form["student_reg"]
            # department=request.form["dept"]
        )
        db.session.add(new_student)
        db.session.commit()
        stud = jsonify(new_student.to_json()) 
        return  (jsonify(new_student.to_json()))
    
@ams.route("/student/<int:id>",methods=["GET","PUT","DELETE"])
def student(id):
    
    if request.method =="GET":
        student=Students.query.get_or_404(id) 
        
        return jsonify(student.to_json() )
    if request.method=="PUT":
        student=Students.query.get_or_404(id) 
        student.fname=request.form["fname"]
        student.mname=request.form["mname"]
        student.sname=request.form["sname"]
        student.password=request.form["password"]
        student.status=request.form["status"]
        student.email=request.form["email"]
        student.yoe=request.form["yoe"]
        student.phone=request.form["phone"]
        student.username=request.form["username"]
        student.student_reg=request.form["student_reg"]
        # student.department=request.form["dept"]
        db.session.add(student)
        db.session.commit()
        return jsonify(student.to_json())
    if request.method=="DELETE":
          student=Students.query.get_or_404(id) 
          db.session.delete(student)
          db.session.commit()
          return {"data": f"Student {student.fname} Deleted successfully"}
    
@ams.route("/about")
def asa():
    pass



# @ams.route("/departments",methods=["GET","POST"])
# def departments():
#      if request.method=="GET":
#         all_dept = Departments.query.all()
#         dept_list = []
#         for dept in all_dept:
#             dept_list.append(dept.to_json())
#         return jsonify(dept_list)
    
#      if request.method=="POST":
#         new_dept=Departments(
#             name=request.form["name"],
#             email=request.form["email"],
#             phone=request.form["phone"],
#             code=request.form["code"]
#             )
#         db.session.add(new_dept)
#         db.session.commit()
#         stud = jsonify(new_dept.to_json()) 
#         return  (jsonify(new_dept.to_json()))



# @ams.route("/department/<int:id>",methods=["GET","PUT","DELETE"])
# def dept(id):
    
#     if request.method =="GET":
#         dept=Departments.query.get_or_404(id) 
        
#         return jsonify(dept.to_json() )
#     if request.method=="PUT":
#         dept=Departments.query.get_or_404(id) 
#         dept.name=request.form["name"]
#         dept.phone=request.form["phone"]
#         dept.email=request.form["email"]
#         dept.code=request.form["code"]
#         return jsonify(dept.to_json())
#     if request.method=="DELETE":
#           dept=Departments.query.get_or_404(id) 
#           db.session.delete(dept)
#           db.session.commit()
#           return {"data": f"Department {dept.name} Deleted successfully"}
    
     
@ams.route("/units",methods=["GET","POST"])
def units():
     if request.method=="GET":
        all_unit = Units.query.all()
        unit_list = []
        for unit in all_unit:
            unit_list.append(unit.to_json())
        return jsonify(unit_list)
    
     if request.method=="POST":
        new_unit=Units(
            name=request.form["name"],
            email=request.form["email"],
            code=request.form["code"],
            status=request.form["status"]
            # department=request.form["department"]
           
            )
        db.session.add(new_unit)
        db.session.commit()
        unit = jsonify(new_unit.to_json()) 
        return  (jsonify(new_unit.to_json()))

@ams.route("/units/<int:id>",methods=["GET","PUT","DELETE"])
def unit(id):
    
    if request.method =="GET":
        unit=Units.query.get_or_404(id) 
        
        return jsonify(unit.to_json() )
    if request.method=="PUT":
        unit=Units.query.get_or_404(id) 
        unit.name=request.form["name"]
        unit.code=request.form["code"]
        unit.email=request.form["email"]
        unit.status=request.form["status"]
        # unit.department=request.form["department"]
        return jsonify(unit.to_json())
    if request.method=="DELETE":
          unit=Units.query.get_or_404(id) 
          db.session.delete(unit)
          db.session.commit()
          return {"data": f"Unit {unit.name} Deleted successfully"}


# @ams.route("/enrollments", methods=["GET","POST"])
# def enrollments():
#      if request.method=="GET":
#         all_enrollment = Enrollment.query.all()
#         units=Units.query.all(all_enrollment.course)
#         students=Students.query.all(all_enrollment.student)
#         enrollment_list = []
#         for enrollment in all_enrollment:
#             enrollment_list.append(enrollment.to_json())
            
#         return render_template('enrolled.html',enrollments=enrollment_list,units=units,students=students)
#         # return jsonify(enrollment_list)

@ams.route("/enrollments", methods=["GET"])
def get_enrollments():
    enrollments = Enrollment.query.all()

    enrollment_list = []
    for enrollment in enrollments:
        student = Students.query.get(enrollment.student_id)
        unit = Units.query.get(enrollment.course_id)

        enrollment_list.append({
            "id": enrollment.id,
            "student_name": student.fname + " " + student.mname + " " + student.sname,
            "course_name": unit.name,
            "course_code": unit.code,
            "student_reg": student.student_reg
        })

    # return jsonify(enrollment_list)
    return render_template('enrolled.html', enrollments=enrollment_list)

@ams.route("/newenrollments",methods=["POST","GET"])
def newenrollment():
    form=EnrollmentForm()
    
    
    if request.method=="POST":
        if form.validate_on_submit():
             new_enrollment=Enrollment(
            # enrollment.id is auto_incremented
            student_id=form.student_id.data,
            course_id=form.course_id.data
            # enrollment_date=request.form["enrollment_date"],
            # status=request.form["status"],
            # department=request.form["department"]
           
            )
        db.session.add(new_enrollment)
        db.session.commit()
        # enrollment = jsonify(new_enrollment.to_json()) 
        # return  (jsonify(new_enrollment.to_json()))
        return redirect (url_for("ams.get_enrollments"))
    return render_template('enroll.html',title='Enroll',form=form)

@ams.route("/enrollments/<int:id>",methods=["GET","PUT","DELETE"])
def enrollment(id):
    
    if request.method =="GET":
        enrollment=Enrollment.query.get_or_404(id) 
        
        return jsonify(enrollment.to_json() )
    if request.method=="PUT":
        enrollment=Enrollment.query.get_or_404(id) 
        enrollment.name=request.form["name"]
        enrollment.code=request.form["code"]
        enrollment.email=request.form["email"]
        enrollment.status=request.form["status"]
        # enrollment.department=request.form["department"]
        return jsonify(enrollment.to_json())
    if request.method=="DELETE":
          enrollment=Enrollment.query.get_or_404(id) 
          db.session.delete(enrollment)
          db.session.commit()
          return {"data": f"enrollment {enrollment.name} Deleted successfully"}
    

# @ams.route("/marks",methods=["GET","POST"])
# def marks():
#      if request.method=="GET":
#         all_marks = Marks.query.all()
#         mark_list = []
#         for mark in all_marks:
#             mark_list.append(mark.to_json())
#         return jsonify(mark_list)


@ams.route("/marks",methods=["GET"])
def get_marks():
    marks=Marks.query.all()
    marks_list=[]
    for mark in marks:
        student = Students.query.get(mark.student_id)
        unit = Units.query.get(mark.course_id)

        marks_list.append({
            "student_name": student.fname + " " + student.mname + " " + student.sname,
            "course_name": unit.name,
            "course_code": unit.code,
            "student_reg": student.student_reg,
            "cat1":mark.cat1,
            "Cat2":mark.Cat2,
            "cat3":mark.cat3,
            "assignment1":mark.assignment1,
            "assignment2":mark.assignment2,
            "assignment3":mark.assignment3,
            "practicals":mark.practicals,
            "mainExam":mark.mainExam,
            "overallmark":mark.overallmarks,
            "student_id":mark.student_id,
            "course_id":mark.course_id
        })
        
    return render_template('viewmarks.html', scores=marks_list)



@ams.route("/newmarks", methods=["GET", "POST"])
def new_marks():
    marks_form=MarksForm()
    if request.method=="POST":
        new_mark=Marks(
            cat1=request.form["cat1"],
            Cat2=request.form["Cat2"],
            cat3=request.form["cat3"],
            assignment1=request.form["assignment1"],
            assignment2=request.form["assignment2"],
            assignment3=request.form["assignment3"],
            practicals=request.form["practicals"],
            mainExam=request.form["mainExam"],
            overallmarks=request.form["overallmarks"],
            student_id=request.form["student_id"],
            course_id=request.form["course_id"]
           
            )
        
        db.session.add(new_mark)
        db.session.commit()
        mark = jsonify(new_mark.to_json()) 
        return redirect(url_for("ams.get_marks"))
    return  render_template("marks.html", marks_form=marks_form)

@ams.route("/marks/<int:id>",methods=["GET","PUT","DELETE"])
def mark(id):
    
    if request.method =="GET":
        mark=Marks.query.get_or_404(id) 
        
        return jsonify(mark.to_json() )
    if request.method=="PUT":
        mark=Marks.query.get_or_404(id) 
        mark.cat1=request.form["cat1"]
        mark.Cat2=request.form["Cat2"]
        mark.cat3=request.form["cat3"]
        mark.assignment1=request.form["assignment1"]
        mark.assignment2=request.form["assignment2"]
        mark.assignment3=request.form["assignment3"]
        mark.practicals=request.form["practicals"]
        mark.mainExam=request.form["mainExam"]
        mark.overallmarks=request.form["overallmarks"]
        mark.course_id=request.form["course_id"]
        mark.student_id=request.form["student_id"]
        return jsonify(mark.to_json())
    if request.method=="DELETE":
          mark=Marks.query.get_or_404(id) 
          db.session.delete(mark)
          db.session.commit()
          return {"data": f"mark {mark.id} Deleted successfully"}


# @ams.route("/results",methods=["GET","POST"])
# def results():
#      if request.method=="GET":
#         all_results = Results.query.all()
#         result_list = []
#         for result in all_results:
#             result_list.append(result.to_json())
#         return jsonify(result_list)
    
#      if request.method=="POST":
#         new_result=Results(
#             firstattempt=request.form["firstattempt"],
#             secondattempt=request.form["secondattempt"],
#             thirdattempt=request.form["thirdattempt"],
#             finalattempt=request.form["finalattempt"],
#             reg=request.form["reg"],
#             course_id=request.form["course_id"]
           
#             )
#         db.session.add(new_result)
#         db.session.commit()
#         result = jsonify(new_result.to_json()) 
#         return  (jsonify(new_result.to_json()))

# @ams.route("/results/<int:id>",methods=["GET","PUT","DELETE"])
# def result(id):
    
#     if request.method =="GET":
#         result=Results.query.get_or_404(id) 
        
#         return jsonify(result.to_json() )
#     if request.method=="PUT":
#         result=Results.query.get_or_404(id) 
#         result.firstattempt=request.form["firstattempt"]
#         result.secondattempt=request.form["secondattempt"]
#         result.thirdattempt=request.form["thirdattempt"]
#         result.finalattempt=request.form["finalattempt"]
#         result.reg.requeest.form["student-id"]
#         result.course_id=request.form["course_id"]
#         return jsonify(result.to_json())
#     if request.method=="DELETE":
#           result=Results.query.get_or_404(id) 
#           db.session.delete(result)
#           db.session.commit()
#           return {"data": f"result {result.name} Deleted successfully"}

# def about():
    # return "<h1>  This is my About Page Enjoy learning about me..... </h1>"
