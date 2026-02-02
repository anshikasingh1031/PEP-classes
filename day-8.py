#square root
# import math
# num=16
# print(math.sqrt(num))

# import math
# num=16
# result=math.sqrt(num)
# print("sqaure root of",num,"is", result)

#power

# import math
# num=99
# result=math.pow(num,2)
# print("sqaure of",num,"is",result)

#floor value
# import math
# num=8.9
# result=math.floor(num)
# print(result)

#ceil
# import math
# num=8.9
# result=math.ceil(num)
# print(result)

#fabs
# import math
# num= -8
# result=math.fabs(num)
# print(result)

#random number
# import random
# dice=random.randint(1,6)
# print(dice)

#for data sets
# import random
# student=["anshika","aishwarya","saumya","archita"]
# selected=random.choice(student)
# print(selected)

#4-digit otp
# import random
# otp=random.randint(1000,9999)
# print(otp)

#date and time
# import datetime
# current=datetime.datetime.now()
# print(current)


#collections counterrrr
# from collections import Counter
# fruits=Counter(["apple","mango","mango","kiwi","kiwi","grapes","pineapple"])
# print(fruits)
# from collections import Counter 
# a="hello"
# con=Counter(a)
# print(con)

# from collections import Counter
# a="python is easy python is fun python is good"
# con=Counter(a.split())
# print(con)

# from collections import Counter
# a="python is easy python is fun python is good"
# con=Counter(a)
# print(con)


# import os
# current_path=os.getcwd()
# print(current_path)

# import os
# item=os.listdir()
# print(item)

#create file
import os
folder_name="myfolder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("file created")
else:
    print("folder is alredy prenst")