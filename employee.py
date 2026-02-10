from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step1
engine=create_engine("sqlite:///company.db")

#step2
Base=declarative_base()

#step3
class Employee(Base):
    __tablename__="employees" 
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department=Column(String)

#step4
Base.metadata.create_all(engine)

#step5
Session=sessionmaker(bind=engine)
session=Session()
e1=Employee(name="nobita",age=20,department="collector")
e2=Employee(name="gian",age=40,department="nalla")
e3=Employee(name="suneo",age=90,department="dalla")
e4=Employee(name="shizuka",age=12,department="cooking")
session.add(e1)
session.add(e2)
session.add(e3)
session.add(e4)
session.commit()

#step6
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)

# #delte one element in that condition
# employees=session.query(Employee).filter(Employee.age>10).all()
# for emp in employees:
#     session.delete(emp)
# session.commit()
# employees=session.query(Employee).all()
# for i in employees:
#     print(i.id,i.name,i.age,i.department)



# #update
# employees=session.query(Employee).filter_by(id==9).first()
# employees.name="anshika"
# session.commit()
# print("updated")
# employees=session.query(Employee).all()
# for i in employees:
#     print(i.id,i.name,i.age,i.department)

# #delete
# employees=session.query(Employee).filter(Employee.id==10).first()
# if employees:
#     session.delete(employees)
#     session.commit()

#     employees=session.query(Employee).all()
# for i in employees:
#     print(i.id,i.name,i.age,i.department)

#delte all emnet in that condition
import os
print(os.getcwd())
print("above is path of database")
employees=session.query(Employee).filter(Employee.age==90).all()
for i in employees:
    session.delete(i)
session.commit()
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)



