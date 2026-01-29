# class Student:
#     print("this is our first class")
# S1=Student()
# print(S1)

# class Student:
#     def __init__(self):
#         self.name="rahul"
# S1=Student()
# print(S1.name)  

# class Student:
#     def __init__(self,fullname):
#         self.name=fullname
# S1=Student("anshika")
# print(S1.name)

# class Student:
#     college_name="lpu"
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
# S1=Student("anshika",50)
# S2=Student("aishwarya",50)
# print(S1.name)
# print(S2.name)
# print(S2.college_name)
# print(S2.college_name)


# class Cars:

#     def __init__(self,model,price):
#         self.name=model
#         self.price=price
# S1=Cars("alto",40000)
# S2=Cars("bmw",400000)
# print(S1.name,S2.price)
# print(S2.name)

# class College:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# S1=College("lpu",90)
# S2=College("cu",80)
# print(S1.name,S1.marks)
# print(S2.name,S1.marks)

# class Student:
#     def __init__(self,name):  
#         self.name=name
#     def hello(self):
#         print("welcome", self.name)
# @staticmethod
# def college_name():
#     print("this is lpu")

#class Student:
    #def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
# S1=Student("anshika",90)
# S2=Student("aishwarya",90)
# print(S1.name,S1.marks)
# print(S2.name,S2.marks)

# @staticmethod
# def collage():
#     print("lpu")
# collage()


# class Student:
#     def __init__(self,marks):
#         self.marks=marks
# s1=Student(100)
# print(s1.marks)


class Student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
S1=Student(100)
print(S1.get_marks())



 

        
        

