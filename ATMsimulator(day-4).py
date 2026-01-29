#atm simulator
file_name="atm_data.txt"
balance=5000       #balnce and pin are global variable that store balnce and pin
pin="1234"
#load data
def load_data():
    #global keyword allows us to modify outside variables
    global balance,pin
    try:
        file=open(file_name,"r")       #open file in read mode
        lines=file.readlines()         #read all lines from file into list
        file.close()                   #close file after all operation
        pin=lines[0].strip()           #1st line contain pin and strip will remove end space
        balance=int(lines[1].strip())    #second line contain balance
    except:                              #if file does not exist or error occurs
        pass                             #pass mean "do nothing "
                                        #program will use default balance and pin

#check balance
def check_balance():
    print("your balance is: ", balance)

 #save data
def save_data():
    file=open(file_name,"w")          # will open file in write mode
    file.write(pin+"\n")               #write pin into the file and go to next  line
    file.write(str(balance))            #write balance as str 
    file.close()                        #close the file

#deposit money
def deposit_money():
    global balance                       #global allows changing original balance
    try:
        amount=int(input("enter the amount to deposit: "))
        balance=balance+amount
        save_data()                #save updated balance to file 
        print("money deposited successfully") 
    except:
        print("please enter number only")


#withdraw money
def withdraw_money():
    global balance
    try:
        amount=int(input("enter the amount you want to withdraw: "))
        if amount>balance:
            print("insufficient money")
        else:
            balance=balance-amount
            save_data()
            print("collect your cash")
    except:
        print("enter number only")

#change pin
def change_pin():
    global pin            
    old_pin=input("enter the old pin: ")    #ask user for old pin 
    if old_pin==pin:                                #check if old pin is correct
        new_pin=input("enter the new pin: ")     #ask new pin 
        pin=new_pin
        save_data()
        print("pin changed")
    else:
        print("incorrect pin")


#main program
def main():
    load_data()        #load data when program starts
    user_pin=input("enter the pin: ")         # ask user to enter pin
    if user_pin!=pin:               #if pin is wrong program will stop
        print("incorrect pin")
        return
    while True:
        print("\n---------ATM MENU--------\n")
        print("1.check balance")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.change pin")
        print("5.exit")
        choice=input("enter your choice: ")
        if choice=="1":
            check_balance()
        elif choice=="2":
            deposit_money()
        elif choice=="3":
            withdraw_money()
        elif choice=="4":
            change_pin()
        elif choice=="5":
            print("thank you for using atm")
            break
        else:
            print("invalid choice")
main()
    
    




