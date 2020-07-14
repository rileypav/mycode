import random
import string
from random import randint

print "Hello, Welcome to the T+ password generator! Your password must be at least six characters long and " \
    "have one special character. Please be sure to only enter whole numbers"

num_letters = int(raw_input("How Many Letters?: "))
num_numbers = int(raw_input("How Many Numbers?: "))
num_special = int(raw_input("How Many Special Characters?: "))
list_of_spec = "!@#$%^&*=+-_?/><.,"

def get_pass_letters(length):
    letters = string.ascii_letters
    pass_letters = ''.join(random.choice(letters) for i in range(length))
    return pass_letters

def get_pass_numbers(l):
    numbers = string.digits
    pass_numbers = ''.join(random.choice(numbers) for i in range(l))
    return pass_numbers

def get_pass_symbols(lnh):
    symbols = list_of_spec
    pass_symbols = ''.join(random.choice(symbols) for i in range(lnh))
    return pass_symbols

password_letters = get_pass_letters(num_letters)
password_numbers = get_pass_numbers(num_numbers)
password_symbols = get_pass_symbols(num_special)

pass_string = password_letters + password_numbers + password_symbols
final_pass = ''.join(random.sample(pass_string, len(pass_string)))

if len(final_pass) < 6:
    print "Password must be longer than 6 characters."
elif num_special == 0:
    print "Must have one special characters"
else:
    print "Your new password is " + final_pass
    print "Thanks again for letting T+ help you with your password generating needs!"