weight = int(input('What is your weight : '))
height = float(input('What is your height : '))

bmi = round(weight/height ** 2)

if bmi <= 18.5:
    print('under weight')
elif bmi > 18.5 and bmi <= 25:
    print('normal weight')
elif bmi > 25 and bmi <= 30:
    print('over weight')
elif bmi > 30 and bmi <= 35:
    print('obes weight')
else:
    print('Cilini obes')
