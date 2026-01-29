''''mobile = {"brand":"oppo","model":24,"price":5000,"stock":20}
laptop = {"dell":"hp","money":7666,"warrenty":"seven"}
print(mobile)
print(mobile["brand"])
print(mobile.get("price"))
print(mobile.keys())
print(mobile.values())
print(mobile.items())
mobile.popitem()
print(mobile)
mobile.pop("price")
print(mobile)
mobile.update({"year":"nine","you":"bad"})
print(mobile)
print(len(mobile))
print(len(laptop))
mobile.update(laptop)
print(mobile)
mobile["brand"]="vivo"
print(mobile)
mobile["waste"]="oppo"
print(mobile)
mobile = laptop.copy()
print(mobile)
'''


'''
contact = {}

while True:
    print("\n---- Contact Book ----")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice here: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact[name] = phone
        print("Contact added successfully")

    # View contacts
    elif choice == "2":
        if contact:
            print("\nSaved Contacts:")
            for name, phone in contact.items():
                print(name, ":", phone)
        else:
            print("No contacts found")

    # Search contact
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contact:
            print("Phone number:", contact[name])
        else:
            print("Contact not found")

    # Delete contact
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contact:
            del contact[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    # Exit
    elif choice == "5":
        print("Exiting contact book...")
        break

    else:
        print("Invalid choice! Please try again.")
  '''      '''
#file handling  write 
file = open("code.txt","w")
file.write("name: rahul \n")
file.write("course: python \n")
file.close()
# read
file=open("code.txt","r")
data= file.read()
print(data)
file.close()
#append
file=open("code.txt","a")
file.write("marks: 90\n")
file.close()

file=open("code.txt","r")
data= file.read()
print(data)
file.close()

file=open("code.txt","r")
data=file.readline()
print(data)
file=open("code.txt","r")
data=file.readlines()
print(data)
print(len(data))
'''
'''
file=open("code.txt","r") 
data=file.read()
print(data.upper()) #upper case
'''
'''
file =open("code.txt","r")
data=file.read()
print("character in file length",len(data))             #charcter lengthhh
file.close()
'''
'''
file=open("code.txt","r")
data=file.read()
word=data.split()              #split the words 
print(word)
file.close()
'''
'''
file=open("code.txt","r")
data=file.read()
count = data.lower().count("rahul")       #count the words   
print(count)
file.close()
'''
'''
file=open("code.txt","r")
data=file.read()
r=data[::-1]                            #reverse string 
print(r)
'''
'''
file=open("code.txt","r")
data=file.read()
r=data.replace("rahul","anshika")                         #replace words 
print(r)
file.close()
'''
file=open("code.txt", "w")
file.write("kabhi khushi kabhi gum\n")
file.write("hum sath stah hain\n")
file.write("dil wale bride le jayege\n")
file.close()


file=open("code.txt", "r")
data=file.read()
s=data.replace(" ","")
print(s)
file.close()

file=open("code.txt","r")
data=file.read()
print(data.replace(" ","     "))
file.close()

file=open("code.txt","r")
data=file.read()
word=data.split()
for w in word:
    print(w[::-1])
    file.close()





        
                
    
