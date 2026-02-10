#import create_engine to connect the database
from sqlalchemy import create_engine
#step1 create base class
engine=create_engine("sqlite:///school.db")
#sql lite database
#file name is school.db
#will be created if not exist
print("database is created")

#import declarative base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker 

#step2
#create base class 
Base=declarative_base()
#base will ne parents of all models
#step3 
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String)
#step4
Base.metadata.create_all(engine) #create all table useing base
#step5
Session=sessionmaker(bind=engine)
session=Session()
s1=Student(id=1,name="rahul",age=20, course="python")
s2=Student(id=2,name="anshika",age=20, course="python")

session.commit()
print("student added")