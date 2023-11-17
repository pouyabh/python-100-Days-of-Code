all = [180, 190, 200, 170, 160, 150, 110, 80, 93, 45]
highest = 0
lower = 0

for no in all:

    if no > highest:
        highest = no

    if no < lower:
        lower = no

print(highest, lower)
