#Stone Paper Scissor Game

import random

print(':::Welcome to Stone|Paper|Scissor:::')
a = int(input('Enter 1 to play: '))
user = 0
computer = 0

while a == 1 and (user < 5 and computer < 5):
    print('Enter 1 to select Stone')
    print('Enter 2 to select Paper')
    print('Enter 3 to select Scissor')
    ch = int(input())
    modes = ['selct any', 'I choose Stone', 'I choose Paper', 'I choose Scissor']
    print(modes[ch])


    if ch > 0:
        if ch==3 and random.randint(1,3)==1:
            print('Uggh!! I lost this round')
            computer += 1
        elif ch == 1 and random.randint(1,3) == 3:
            print('Yes!!! I win this round')
            user += 1
        elif ch > random.randint(1,3):
            print('Yes!!! I win this round')
            user += 1
        elif ch < random.randint(1,3):
            print('Uggh!! I lost this round')
            computer += 1
        else:
            print('Game draw')
    print('---Scores---')
    print('User: {}'.format(user))
    print('Computer: {}'.format(computer))
    print('----------')

def Winner():
    if user == 5:
        print("You won the match, I'll see you next time")
    elif computer == 5:
        print("Better luck next time :)")

Winner()
    
    
    
