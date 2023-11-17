import random

letters = ['a', 'b', 'c', 'd']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^']

no_generator = int(input('count of password : '))
password = ''

for char in range(1, no_generator+1):
    password += random.choice(letters)

for char in range(1, no_generator+1):
    password += str(random.choice(number))

for char in range(1, no_generator+1):
    password += str(random.choice(symbols))

print(password)
