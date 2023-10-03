# Password Generator Script
# By nono_t27
# This basically generates a random password in a nutshell. 

import random

choice = [1, 2] # 1 adds a number & 2 adds a string

while True:
    password = ""
    password_length = input("Enter the length of your password: ")
    
    if not password_length.isdigit() or int(password_length) <= 0:
        print("Invalid number or option. Please enter a positive integer.")
        continue
    
    password_length = int(password_length)
    random_element = random.choice(choice)  # chooses between the numbered choices
    
    for i in range(password_length):
        # Add number.
        if random_element == 1:
            password += str(random.randint(0, 9)) # Generates the number
        
        # Add string.
        elif random_element == 2:
            password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*-_=+") # Chooses between these select number of strings.
        
        random_element = random.choice(choice)  # chooses between the numbered choices
    
    first_generated_password = password
    print("Your new generated password:", password)
    go_back = input("Would you like to go back and generate the new one? (Type any key for yes n for no): ")
    password = "" # Reset the password.

    if go_back.lower() == "n":
        print("Enjoy your new password")
        break