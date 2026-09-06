import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','*']

print("Welcome to Python password Generatore!")

nr_letters = int(input("How many letters do you want?\n"))
nr_symbols = int(input("How many symbols do you want\n"))
nr_numbers = int(input("How many symboles do you want?\n"))
password = []
for char in range(0, nr_letters ):
    password.append(random.choice(letters))
for char in range(0, nr_numbers):
    password.append(random.choice(numbers))
for char in range(0, nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
print(password)

new_password = ""
for char in password:
    new_password += char
print(f"Your password is {new_password}")