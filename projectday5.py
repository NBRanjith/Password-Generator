import random
import string

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letters_count = int(input("how many letters would you like?\n"))
symbols_count = int(input("how many symbols would you like?\n"))
numbers_count = int(input("how many numbers would you like?\n"))
upper_case = list(string.ascii_uppercase)
lower_case = list(string.ascii_lowercase)
alphabets = upper_case + lower_case
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@','#','$','%','&','*', '+']

#easy_level

# password = ""
#
# for char in range(0, letters_count):
#     #1-4
#     password += random.choice(alphabets)
# for char in range(0, symbols_count):
#     #1-4
#     password += random.choice(symbols)
# for char in range(0, numbers_count):
#     #1-4
#     password += random.choice(numbers)
# print(password)


#hardlevel

password_list= []

for char in range(0, letters_count):
    #1-4
    password_list.append(random.choice(alphabets))
for char in range(0, symbols_count):
    #1-4
    password_list.append(random.choice(symbols))
for char in range(0, numbers_count):
    #1-4
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

final_pass = ''
for char in password_list:
    final_pass += char
print(final_pass)