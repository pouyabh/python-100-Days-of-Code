import random

rand_No = random.randint(1, 3000)
rand_Float = random.random()

print(rand_No, rand_Float)

if random.randint(0, 1):
    print('Head')
else:
    print('tile')


all = ['a', 'b', 'c', 'd', 'e']

all.append('f')
all.insert(0, 'g')

print(all)

name="pouya,bh"

print(name.split(','))
