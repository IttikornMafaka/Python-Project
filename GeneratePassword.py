import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = [] #List Data from input
for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letter))
for char in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbol))
for char in range(1,nr_numbers + 1):
    password_list.append(random.choice(number))
random.shuffle(password_list)

# Convert List to char
password = ""
for char in password_list :
    password += char
print(password)
