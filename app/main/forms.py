from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,FloatField,IntegerField


class MarksForm(FlaskForm):
    cat1=FloatField("CAT 1" )
    Cat2=FloatField("CAT 2" )
    cat3=FloatField("CAT 3" )
    assignment1=FloatField("Assignment 1" )
    assignment2=FloatField("Assignment 2" )
    assignment3=FloatField("Assignment 3" )
    practicals=FloatField("Practials" )
    mainExam=FloatField("MainExam" )
    overallmarks=FloatField("Overall" )
    submit=SubmitField("SUBMIT")

    



class EnrollmentForm(FlaskForm):
    course_id=StringField("course code")
    student_id=StringField("Registration number")
    subit=SubmitField("Enroll ")