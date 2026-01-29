#inheritance one class uses another class properties
# class Human:
#     def eat(self):
#         print("human can eat ")
# class Student(Human):
#     def study(self):
#         print("student can study")
# s1=Student()
# s1.eat()

# class Animal:
#     def sound(self):
#         print("all animal can speak")
# class Dog(Animal):
#     def pet(self):
#         print("all dogs can bark")
# s1=Dog()
# s1.sound()

# class Nokia:
#     def old_mobile(self):
#         print("old mobile are only for phone calls")
# class Iphone(Nokia):
#     def new_phone(self):
#         print("new mobiles are good for everthing")
# s1=Iphone()
# s1.old_mobile()

#child constructor
# class Parent:
#     def __init__(self):
#         print("this is parent constructor")
# class Child(Parent):
#     def __init__(self):
#         print("this is child constructor")

#method overriding
# class Parent:
#     def work(self):
#         print("i will go to work")
# class Child(Parent):
#     def work(self):
#         print("i will go to school")
# s1=Child()
# s1.work()

#super methof
# class Parent:
#     def __init__(self):
#         print("i am parent")
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#     print("i am child")
# s1=Child()

# class Teacher:
#     def teaching(self):
#         print("teacher is teaching")
# class Coder:
#     def coding(self):
#         print("coder is coding")
# class Student(Teacher,Coder):
#     pass
# s1=Student()
# s1.coding()
# s1.teaching()


# class Parent:
#     def __init__(self):
#         self.__x=10
# class Child(Parent):
#     def show(self):
#         print(self.__x)
# s1=Child()
# s1.show()


# class Parent:
#     def __init__(self):
#         self._x=100
# class Child(Parent):
#     def show(self):
#         print(self._x)
# s1=Child()
# s1.show()

#question-1
# class Parent:
#     def __init__(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name
# class Student(Parent):
#     def show_name(self):
#         print(self.get_name())
# s1= Student("sam")
# s1.show_name()

#question-2
# class Account:
#     def __init__(self,balance):
#         self._balance=balance
#     def show_balance(self):
#         print(self._balance)
# class Saving(Account):
#     def add_money(self,amount):
#         self._balance+=amount
#         print("money added: ", amount)
#         print("updated balnce",self._balance)
# s1=Saving(40)
# # s1.show_balance()
# s1.add_money(10)
# s1.show_balance()


#digonal 
class A:
    print("a")
class B(A):
    print("b")
class C(A):
    print("c")
class D(B,C):
    print("d")
pass


