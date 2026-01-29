# number=[10,20,30,40]
# for i in number:
#     print(i) 

# fruit=[]
# print(fruit)
# fruit.append("apple")
 # print(fruit)

 #make list and find sum
# number=[10,20,30,40]
# total=0
 # for i in number:
# #     total=total+i
# # print(total)

# # # # # # # #reverse string
# # # # # # num=[10,20,100,150]
# # # # # # reverse_list=num[::-1]
# # # # # # print(reverse_list)

# # # # # #remove duplicate from list
# # # # # num=[1,1,2,2,3,4,5,3,2]
# # # # # unique=[]
# # # # # for i in num:
# # # # #     if i not in unique:
# # # # #         unique.append(i)
# # # # # print(unique)

# # # # #crete tupple and accese its lemets

# # # # colors=("pink", "black","red", "brown")
# # # # print(colors[0])
# # # # print(colors[3])
# # #  #list to tuple 
# # # number=[1,2,3,4,5]
# # # print(type(number))
# # # change=tuple(number)
# # # print(change)
# # # print(type(change))

# # #tuple to set
# # colors=("pink", "red","brown","black")
# # print(type(colors))
# # change=list(colors)
# # print(change)
# # print(type(change))

# #list to sets

# number=[1,1,2,2,3,4,5,3,2]
# print(number)
# print(type(number))
# change=set(number)
# print(change)
# print(type(change))
# list=list(change)
# print(change) 


# #convert dict into set
# student={"name":"anshika", "age":20}
# change=set(student)
# print(change)

 #set to dict
# colours={"pink","red","brown","black"}
# change=dict.fromkeys(colours,100)
# print(change)
# print(type(change))


#catching a specific error
# try:
#     x= int(input("enter the number: "))
#     print(10/x)
# except ZeroDivisionError:
#     print("you cannot divide by 0")
# except ValueError:
#     print("enter only number")

#else block
# try:
#     num=int(input("enter the number:"))
#     print(10/num)
# except:
#     print("error occured")
# else:
#     print("no error")


# class LowBalanceError(Exception):
#     pass
# balance=500
# withdraw=int(input("enter the amount: "))
# if withdraw>balance:
#     raise LowBalanceError("insufficient balance")
# else:
#     print("withdraw successfully")


# try:
#     num=int(input("enter the number: "))
#     print(100/num)
# except ValueError:
#     print("enter only number not string")
# except ZeroDivisionError:
#     print("cannot divide by 0")
# else:
#     print("done")


# try:
#     try:
#         print(100/0)
#     finally:
#         print("inner finally")
# except ZeroDivisionError:
#     print("outer exception")
# finally:
#     print("outer finally")


# def test():
#     try:
#         return 10
#     finally:
#         return 20
# print(test())

# try:
#     try:
#         x=int("abc")
#     except ValueError:
#         print("inner")
#         raise
# except Exception:
#     print("outer")

# def test():
#     try:
#         return 10
#     except: 
#         return 20
#     finally:
#         return 50
# print(test())

# age = int(input("enter the age: "))
# if age<18:
#     raise ValueError("age must be 18 or above")
# print("you can vote")


# print(True+True+False)
# print("5"+"7")
# print("5"*10)

# def update(lst):
#     lst.append(10)
# nums = [1,2,3]
# update(nums)
# print(nums)
# t=(1,2,3)
# t=t+(4,)
# print(t)


# def change(x):
#     x+=10
# x=5
# change(x)
# print(x)


# i=1
# while i<10:
#     i*=3
#     print(i)

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)

# for i in range (3):
#     print(3)
# else:
#     print("done")

#move all zero to end
# nums=[0,0,1,2,3]
# result=[]
# zero_count=0
# for n in nums:
#     if n==0:
#         zero_count+=1
#     else:
#         result.append(n)
# for i in range(zero_count):
#     result.append(0)
# print(result)



#palindrome 
# text="anshika"
# left=0
# right=len(text)-1
# is_Palindrome=True
# while left<right:
#     if text[left]!=text[right]:
#         is_Palindrome=False
#         break
#     left+=1
#     right-=1
# print(is_Palindrome)


#find longest word in sentence
sentence="python make programming fun"
word=sentence.split()
longest=""
for i in word:
    if len(i)>len(longest):
        longest=i
print(longest)





