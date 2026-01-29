
# # # # # # # # # # ''''x= int(input("enter you age: "))
# # # # # # # # # # if(x>=18):
# # # # # # # # # #     print("you are eligible")
# # # # # # # # # # else:
# # # # # # # # # #     print("you are not")
# # # # # # # # # #     '''

# # # # # # # # # # '''x = int(input("enter the number: "))
# # # # # # # # # # if(x%2==0):
# # # # # # # # # #     print("number is even")
# # # # # # # # # # else:
# # # # # # # # # #     print("number is odd")
# # # # # # # # # #     '''

# # # # # # # # # # '''marks = int(input("enter marks"))
# # # # # # # # # # if (marks >=90):
# # # # # # # # # #     print("a grade")
# # # # # # # # # # elif (marks>=70):
# # # # # # # # # #     print("b garde")
# # # # # # # # # # elif (marks>=50):
# # # # # # # # # #     print("c garde") 
# # # # # # # # # # else:
# # # # # # # # # #     print("fail")
# # # # # # # # # # '''

# # # # # # # # # # '''x = int(input("enter the x number: "))
# # # # # # # # # # y = int(input("enter the y number: "))
# # # # # # # # # # if (x>y):
# # # # # # # # # #     print("x is greater")
# # # # # # # # # # elif (y>x):
# # # # # # # # # #     print("y is larger")
# # # # # # # # # # else:
# # # # # # # # # #     print("both are equal")
# # # # # # # # # #     '''

# # # # # # # # # # '''light =str(input("enter light colour"))
# # # # # # # # # # if light == "red":
# # # # # # # # # #     print("wait")
# # # # # # # # # # elif light == "yellow":
# # # # # # # # # #     print("get ready")
# # # # # # # # # # elif light == "green":
# # # # # # # # # #     print("go")
# # # # # # # # # # else:
# # # # # # # # # #     print("invalid")
# # # # # # # # # #     '''

# # # # # # # # # # '''units = int(input("enter the units: "))
# # # # # # # # # # if units <=100:
# # # # # # # # # #     bill = units * 2
# # # # # # # # # #     print(bill)
# # # # # # # # # # elif units <=200:
# # # # # # # # # #     bill = units*2
# # # # # # # # # #     print(bill)
# # # # # # # # # # elif units <=500:
# # # # # # # # # #     bill= units*2
# # # # # # # # # #     print(bill)
# # # # # # # # # # else:
# # # # # # # # # #     print("invalid")
# # # # # # # # # #     '''

# # # # # # # # # # #calculator
# # # # # # # # # # '''
# # # # # # # # # # a = int(input("enter 1st number: "))
# # # # # # # # # # b = int(input("enetr 2nd number: "))
# # # # # # # # # # op = (input("enter the operation (+,-,*,/): "))
# # # # # # # # # # if op == "+":
# # # # # # # # # #     print(a+b)
# # # # # # # # # # elif op =="-":
# # # # # # # # # #     print(a-b)
# # # # # # # # # # elif op =="*":
# # # # # # # # # #     print(a*b)
# # # # # # # # # # elif op == "/":
# # # # # # # # # #     if b!=0:
# # # # # # # # # #         print(a/b)
# # # # # # # # # #     else:
# # # # # # # # # #         print("cannot divide by 0")
# # # # # # # # # # else:
# # # # # # # # # #     print("invalid operation")
# # # # # # # # # # '''


# # # # # # # # # # '''years = int(input("enter the year: "))
# # # # # # # # # # if years % 400 == 0:
# # # # # # # # # #     print("leap year")
# # # # # # # # # # else:
# # # # # # # # # #     print("not a leap year")
# # # # # # # # # #     '''


# # # # # # # # # # # #for loop
# # # # # # # # # # # for i in range(1, 7):
# # # # # # # # # # #     print(i)

# # # # # # # # # # # for i in range(1,15):
# # # # # # # # # # #     if(i%2!=0):
# # # # # # # # # # #         print(i)
# # # # # # # # # # # rows = int(input("enter row: "))
# # # # # # # # # # # for i in range (1, rows+1):
# # # # # # # # # # #     print("*" * i)

# # # # # # # # # # for i in range (1,11):
# # # # # # # # # #  print("7 x ", i, "=", 7*i)

# # # # # # # # # #  name= "anshika"
# # # # # # # # # #  for ch in name:
# # # # # # # # # #   print(ch)

# # # # # # # # # for i in range(10,0,-1):
# # # # # # # # #     print(i)

# # # # # # # # for i in range(1,21):
# # # # # # # #     if i%2==0:
# # # # # # # #         print(i)

# # # # # # # for i in range(1,20):
# # # # # # #  print(i*i)

# # # # # # num = int(input("enter the number: "))
# # # # # # for i in range (1,11):
# # # # # #     print(num, "x", i, "=", num*i)


# # # # # count=0
# # # # # for i in range (1,101):
# # # # #     print(i)
# # # # #     count+=1
# # # # #     print(count)

# # # # total=0
# # # # for i in range (1, 11):
# # # #     total+=i
# # # #     print(total)

# # # text = input("enter name: ")

# # # for ch in text:
# # #     print(ch)
# # #     count=0
# # #     count+=1
# # #     print(count)

# # num = int(input("enter number: "))
# # fact=1
# # for i in range (1, num+1):
# #     fact *=i
# #     print(fact)

# even = 0
# odd = 0
# i = int(input("enter num "))
# for i in range (1,51):
#     if i%2==0:
        
#        print("even number")
#     else:
        
#         print("odd")

# while loop
# num=int(input("enter the number: "))
# i=1
# while i<=10:
#  print(num,"x", i, "=", num*i)
#  i+=1

#print num from 1-10
# i=1
# while i<=10:
#     print(i)
#     i+=1

#print num from 10-1
# i=10
# while i>=1:
#     print(i)
#     i-=1

#couter bumber from 1 -50
# i=1
# count=0
# while i<=50:
    
#     count+=1
#     i+=1
# print(count)

#reverse a number
# num=int(input("enter the number: "))
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num//=10
# print(reverse)


#check even or odd until user enter 0
num=int(input("enter the number: "))
while num !=0:
    if num%2==0:
        print("even")
    else:
        print("odd")
    num=int(input("enter the number: "))
    
print("loop ended")




