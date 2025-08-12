print("I'm gonna be the King of the Hackers/Programmer!\nI'm gonna surpass my limits right here, right now~")

import random
import string

def gen_pass(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_characters:
        char += special_char

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(char)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_char:
            has_special = True
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special
        
    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == 'y'
has_special = input("Do you want to have special characters (y/n)? ").lower() == 'y'
pwd = gen_pass(min_length,has_number,has_special)

print("The generated password is:",pwd)