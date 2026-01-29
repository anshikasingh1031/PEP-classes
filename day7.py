# #abstraction
# class Payment:
#     def pay(self,amount):
#         pass
# class UPI(Payment):
#     def pay(self,amount):
#         print("paid using upi: ",amount)
# class Card(Payment):
#     def pay(self,amount):
#         print("paid using card", amount)
# class Cash(Payment):
#     def pay(self,amount):
#         print("paid using cash",amount)
# obj=UPI()
# obj=Card()
# obj.pay(12)



# #INTERFACE
# from abc import ABC, abstractmethod 

# class Payment:
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class UPI(Payment):
#     def pay(self, amount):
#         print("paid using UPI:", amount)

# class Card(Payment):
#     def pay(self, amount):
#         print("paid using Card:", amount)

# class Cash(Payment):
#     def pay(self, amount):
#         print("paid using Cash:", amount)


# # Object creation
# obj = Card()
# obj.pay(12)


class Course:
    def course_info(self):
        print("course information")
    def duration(self):
        pass
       
class ExamInterface:
    def exam_type(self):
        pass

class Python_course(Course,ExamInterface):
    def duration(self):
        print("course duration is 3 months")
    def exam_type(self):
        print("exam is practical based")
        
class JavaCourse(Course,ExamInterface):
    def duration(self):
        print("course duration is 2 months")
    def exam_type(self):
        print("exam is theory based")
obj = Python_course()
obj.duration()