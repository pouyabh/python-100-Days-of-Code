import random

all = ['rock', 'paper', 'scissors']

computer_choise = random.choice(all)
user_choise = int(input('insert your choise: (0=>rock,1=>paper)'))


if user_choise == 1:
    user_choise = 'rock'
elif user_choise == 2:
    user_choise = 'paper'
elif user_choise == 3:
    user_choise = 'scissors'
else:
    print('invalid input')

if computer_choise == user_choise:
    print('draw')
elif computer_choise == 'rock' and user_choise == 'paper':
    print('you win')
elif computer_choise == 'rock' and user_choise == 'scissors':
    print('you lose')
elif computer_choise == 'paper' and user_choise == 'rock':
    print('you lose')
elif computer_choise == 'paper' and user_choise == 'scissors':
    print('you win')
elif computer_choise == 'scissors' and user_choise == 'rock':
    print('you win')
elif computer_choise == 'scissors' and user_choise == 'paper':
    print('you lose')
else:
    print('sth Wrong')

print(computer_choise, user_choise)
