import random
import string
import sys
from random import randint

print "Hello, Welcome to the T+ password generator! Your password must be at least six characters long and " \
    "have one special character. Please be sure to only enter whole numbers."

raw_int_letters = (raw_input("How Many Letters?: "))
raw_int_numbers = (raw_input("How Many Numbers?: "))
raw_int_specials = (raw_input("How Many Special Characters?: "))
list_of_spec = "!@#$%^&*=+-_?/><.,"

def int_check(input):
    if input in string.ascii_letters:
        print "Please be sure to enter only numbers."
        sys.exit()
    else:
        return int(input)

num_letters = (int_check(raw_int_letters))
num_numbers = (int_check(raw_int_numbers))
num_specials = (int_check(raw_int_specials))

def get_pass_letters(length):
    letters = string.ascii_letters
    pass_letters = ''.join(random.choice(letters) for i in range(length))
    return pass_letters

def get_pass_numbers(l):
    numbers = string.digits
    pass_numbers = ''.join(random.choice(numbers) for i in range(l))
    return pass_numbers8

def get_pass_symbols(lnh):
    symbols = list_of_spec
    pass_symbols = ''.join(random.choice(symbols) for i in range(lnh))
    return pass_symbols

password_letters = get_pass_letters(num_letters)
password_numbers = get_pass_numbers(num_numbers)
password_symbols = get_pass_symbols(num_specials)

pass_string = password_letters + password_numbers + password_symbols
final_pass = ''.join(random.sample(pass_string, len(pass_string)))

if len(final_pass) < 6:
    print "Password must be longer than 6 characters."
elif num_specials == 0:
    print "Must have one special characters"
else:
    print "Your new password is " + final_pass
    print "Thanks again for letting T+ help you with your password generating needs!"