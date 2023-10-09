from faker import Faker
from . import db
from .models import Students, Units

fake = Faker()

def students(count=100):
    i = 0
    while i < count:
        u = Students(
            fname=fake.name().split()[0],
            mname=fake.name().split()[0],
            sname=fake.name().split()[0],
            email=fake.email(),
            username=fake.user_name(),
            password=fake.random_number(),
            yoe=fake.past_date(),
            phone=fake.random_number(digits=10),
            status="active",
            student_reg=fake.random_number(digits=4)
        )
        db.session.add(u)
        i += 1
        try:
            db.session.commit()
        except Exception as e:
            print(e)
        db.session.rollback()
        
def units(count=40):
    i = 0
    while i < count:
        u = Units(
            fname=fake.name().split()[0],
            mname=fake.name().split()[0],
            sname=fake.name().split()[0],
            email=fake.email(),
            username=fake.user_name(),
            password=fake.random_number(),
            yoe=fake.past_date(),
            phone=fake.random_number(digits=10),
            status="active",
            student_reg=fake.random_number(digits=4)
        )
        db.session.add(u)
        i += 1
        try:
            db.session.commit()
        except Exception as e:
            print(e)
        db.session.rollback()
        
  