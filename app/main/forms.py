from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FloatField, IntegerField, SelectField, validators
from ..models import Students, Units, Enrollments,Years
from .. import db

class MarksForm(FlaskForm):
    enrollment_id = SelectField('Student Name', coerce=int)
    # student_id = SelectField('Students', coerce=int)
    # course_id = SelectField('course', coerce=int)
    cat1 = FloatField("Cat 1")
    Cat2 = FloatField("Cat 2")
    cat3 = FloatField("Cat 3")
    assignment1 = FloatField("Assignment 1")
    assignment2 = FloatField("Assignment 2")
    assignment3 = FloatField("Assignment 3")
    practicals = FloatField("Practials")
    mainExam = FloatField("Main Exam")
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)
        enrollm=Enrollments.query.filter_by(course_id=14)
        units=Units.query.filter_by(id=2)
        # unit = units.query.get(enrollm.course_id)
        print(units)
        

        # self.student_id.choices = [(students.id, students.fname + "  " + students.sname + " - " + students.student_reg)
        #                            for students in Students.query.all()]
        # self.course_id.choices = [(units.id, units.code + " - " + units.name)
        #                          for units in Units.query.all()]
        self.enrollment_id.choices = [(enrollments.id, enrollments.students_id.fname + " " + enrollments.students_id.mname + " " +" - "+ enrollments.unit_id.name )
                                      for enrollments in Enrollments.query.filter_by(course_id=14)]

    def validate_overallmarks(form, field):
        cat1 = form.cat1.data
        Cat2 = form.Cat2.data
        cat3 = form.cat3.data
        assignment1 = form.assignment1.data
        assignment2 = form.assignment2.data
        assignment3 = form.assignment3.data
        practicals = form.practicals.data
        mainExam = form.mainExam.data

        # Calculate overallmarks here (customize this calculation as per your requirements)
        overallmarks = (cat1 + Cat2 + cat3 + assignment1 + assignment2 + assignment3 + practicals + mainExam)

        # Assign the calculated value to the field's data
        field.data = overallmarks

# class EnrollmentForm(FlaskForm):
#     student_id = SelectField('Students', coerce=int)
#     course_id = SelectField('course', coerce=int)
#     submit = SubmitField("Enroll")

#     def __init__(self, *args, **kwargs):
#         super(EnrollmentForm, self).__init__(*args, **kwargs)

#         self.student_id.choices = [(students.id, students.fname + "  " + students.sname + " - " + students.student_reg)
#                                    for students in Students.query.all()]
#         self.course_id.choices = [(units.id, units.code + " - " + units.name)
#                                  for units in Units.query.all()]

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
