from . import ams
from flask import request,jsonify
from .. import db
from ..models import Students,Units,Departments,Marks,Results


@ams.route("/")
@ams.route("/home")
def home():
    return "<h1><i>Hello , rekindling some old flask tutorials</i></h1> "

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
            status=request.form["status"]
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



@ams.route("/departments",methods=["GET","POST"])
def departments():
     if request.method=="GET":
        all_dept = Departments.query.all()
        dept_list = []
        for dept in all_dept:
            dept_list.append(dept.to_json())
        return jsonify(dept_list)
    
     if request.method=="POST":
        new_dept=Departments(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"],
            )
        db.session.add(new_dept)
        db.session.commit()
        stud = jsonify(new_dept.to_json()) 
        return  (jsonify(new_dept.to_json()))



@ams.route("/department/<int:id>",methods=["GET","PUT","DELETE"])
def dept(id):
    
    if request.method =="GET":
        dept=Departments.query.get_or_404(id) 
        
        return jsonify(dept.to_json() )
    if request.method=="PUT":
        dept=Departments.query.get_or_404(id) 
        dept.name=request.form["name"]
        dept.phone=request.form["phone"]
        dept.email=request.form["email"]
        return jsonify(dept.to_json())
    if request.method=="DELETE":
          dept=Departments.query.get_or_404(id) 
          db.session.delete(dept)
          db.session.commit()
          return {"data": f"Department {dept.name} Deleted successfully"}
    
     
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
        return jsonify(unit.to_json())
    if request.method=="DELETE":
          unit=Units.query.get_or_404(id) 
          db.session.delete(unit)
          db.session.commit()
          return {"data": f"Unit {unit.name} Deleted successfully"}

@ams.route("/marks",methods=["GET","POST"])
def marks():
     if request.method=="GET":
        all_marks = Marks.query.all()
        mark_list = []
        for mark in all_marks:
            mark_list.append(mark.to_json())
        return jsonify(mark_list)
    
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
            overallmarks=request.form["overallmarks"]
           
            )
        db.session.add(new_mark)
        db.session.commit()
        mark = jsonify(new_mark.to_json()) 
        return  (jsonify(new_mark.to_json()))

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
        return jsonify(mark.to_json())
    if request.method=="DELETE":
          mark=Marks.query.get_or_404(id) 
          db.session.delete(mark)
          db.session.commit()
          return {"data": f"mark {mark.id} Deleted successfully"}


@ams.route("/results",methods=["GET","POST"])
def results():
     if request.method=="GET":
        all_results = Results.query.all()
        result_list = []
        for result in all_results:
            result_list.append(result.to_json())
        return jsonify(result_list)
    
     if request.method=="POST":
        new_result=Results(
            firstattempt=request.form["firstattempt"],
            secondattempt=request.form["secondattempt"],
            thirdattempt=request.form["thirdattempt"],
            finalattempt=request.form["finalattempt"]
           
            )
        db.session.add(new_result)
        db.session.commit()
        result = jsonify(new_result.to_json()) 
        return  (jsonify(new_result.to_json()))

@ams.route("/results/<int:id>",methods=["GET","PUT","DELETE"])
def result(id):
    
    if request.method =="GET":
        result=Results.query.get_or_404(id) 
        
        return jsonify(result.to_json() )
    if request.method=="PUT":
        result=Results.query.get_or_404(id) 
        result.firstattempt=request.form["firstattempt"]
        result.secondattempt=request.form["secondattempt"]
        result.thirdattempt=request.form["thirdattempt"]
        result.finalattempt=request.form["finalattempt"]
        return jsonify(result.to_json())
    if request.method=="DELETE":
          result=Results.query.get_or_404(id) 
          db.session.delete(result)
          db.session.commit()
          return {"data": f"result {result.name} Deleted successfully"}

def about():
    return "<h1>  This is my About Page Enjoy learning about me..... </h1>"