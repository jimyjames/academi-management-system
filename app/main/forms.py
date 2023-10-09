from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FloatField,IntegerField,SelectField
from ..models import Students,Units,Enrollments,Years


class MarksForm(FlaskForm):
    enrollment_id=SelectField('Enrollment', coerce=int)
    student_id=SelectField('Students',coerce=int)
    course_id=SelectField('course', coerce=int)
    cat1=FloatField("CAT 1" )
    Cat2=FloatField("CAT 2" )
    cat3=FloatField("CAT 3" )
    assignment1=FloatField("Assignment 1" )
    assignment2=FloatField("Assignment 2" )
    assignment3=FloatField("Assignment 3" )
    practicals=FloatField("Practials" )
    mainExam=FloatField("MainExam" )
    overallmarks=FloatField("Overall" )
    submit = SubmitField("Add")

    def __init__(self, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)

        self.student_id.choices=[(students.id, students.fname +  "  " +students.sname +" - " + students.student_reg ) 
                                for students in Students.query.all()]
        self.course_id.choices=[(units.id, units.code + " - "+ units.name ) 
                                for units in Units.query.all()]
        self.enrollment_id.choices = [(enrollments.id)
                                      for enrollments in Enrollments.query.all()]
    



class EnrollmentForm(FlaskForm):
    student_id = SelectField('Students', coerce=int)
    module_info = SelectField('Module Information', coerce=int)
    submit = SubmitField("Enroll")

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)

        self.student_id.choices = [(student.id, f"{student.fname} {student.sname} - {student.student_reg}")
                                   for student in Students.query.all()]

        # Fetch year and semester information from the database
        semester_choices = [(year.id, f" Year {year.year} - Semester {year.semester}")
                            for year in Years.query.all()]
        self.module_info.choices = semester_choices
