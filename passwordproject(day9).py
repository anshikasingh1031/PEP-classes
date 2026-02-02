#import modules
import random      #random value
import string     
import math        
import os          # for file handling

#generate a random password
def generate_password(length=8):
    # all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # randomly choose characters
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

#check password strength
def check_strength(password):
    length = len(password)   
    
    #strength score 
    score = math.log2(len(set(password))) * length
    
    # check password  strength
    if score < 20:
        strength = "Weak"
    elif score < 40:
        strength = "Medium"
    else:
        strength = "Strong"
        
    return score, strength

#main code
password = generate_password()          
score, strength = check_strength(password)  

#output
print("Generated Password:", password)
print("Password Length:", len(password))
print("Strength Score:", round(score, 2))
print("Password Strength:", strength)

#save result into a file
file_name = "password_result.txt"
with open(file_name, "w") as file:
    file.write("Generated Password: " + password + "\n")
    file.write("Password Length: " + str(len(password)) + "\n")
    file.write("Strength Score: " + str(round(score, 2)) + "\n")
    file.write("Password Strength: " + strength + "\n")

print("\nResult saved in file:", os.path.abspath(file_name))