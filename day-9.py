# write a regrex to validate 10 digits mobile num
# import re
# mobile="8234567892"
# pattern=r"^[0-9]{10}$"
# if re.match(pattern,mobile):
#     print("valid")
# else:
#     print("invalid")


#contact me at test@gmail.com or admin@yahoo.in
# import re
# text="contact me at test@gmail.com or admin@yahoo.in"
# emails=re.findall(r"[a-zA-Z0-9._] +@[a-zA-Z]+\.[a-zA-Z]{2,}",text)
# print(emails)

#extract email from a string other approch
# import re
# text="contact me at test@gmail.com or admin@yahoo.in"
# pattern=r"[\w.-]+@[\w.-]+\.\w+"
# emails=re.findall(pattern,text)
# print(emails)


#extract all the numbers from the string
# import re
# string="order123 price123 quantity40"
# pattern=re.findall(r"\d+",string)
# print(pattern)

#strong passs
# import re
# password=input("enter the password: ")
# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
# if re.match(pattern,password):
#     print("pass valid")
# else:
#     print("not valid")

#PAN card number    ABCDE1234F
# import re
# pan=input("enter pan num: ")
# pattern=r"^[A-Z]{5}\D{4}[A-Z]{1}$"
# if re.match(pattern,pan):
#     print("valid")
# else:
#     print("not valid")

#ipv4
# import re
# add=input("enter ip add: ")
# pattern=r"^\d{3}\.\d{3}\.\d{3}\.\{3}$"
# if re.match(pattern,add):
#     print("valid")
# else:
#     print("not valid")

#IPV6--------------------------------------------------
# import re
# ip = input("enter your ipv6 address:")
# pattern = r'^(([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(([0-9A-Fa-f]{1,4}:){1,7}:)|(([0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,5}(:[0-9A-Fa-f]{1,4}){1,2})|(([0-9A-Fa-f]{1,4}:){1,4}(:[0-9A-Fa-f]{1,4}){1,3})|(([0-9A-Fa-f]{1,4}:){1,3}(:[0-9A-Fa-f]{1,4}){1,4})|(([0-9A-Fa-f]{1,4}:){1,2}(:[0-9A-Fa-f]{1,4}){1,5})|([0-9A-Fa-f]{1,4}:)((:[0-9A-Fa-f]{1,4}){1,6})|(:)((:[0-9A-Fa-f]{1,4}){1,7}|:))$'
# if re.match(pattern,ip):
#     print("valid ip")
# else:
#     print("invalid ip")

#hexadecimal
# import re
# hexa=input("enter the value: ")
# pattern=r'^[A-F]{2}\d{4}$'
# if re.match(pattern,hexa):
#     print("valid")
# else:
#     print("not")

