# Rock Paper Scissor

import random

CompTurn = random.randint(1,3)
if CompTurn == 1:
    CompChoice = 'r'
elif CompTurn == 2:
    CompChoice = 'p'
elif CompTurn == 3:
    CompChoice = 's'

YourChoice = input("Choose : Rock(r or R) Paper(p or P) Scissor(s or S) : ")

def game(CompChoice, YourChoice):
    if CompChoice == 'r':
        if YourChoice == 'r'or YourChoice == 'R':
            print("Tie")
        elif YourChoice == 'p'or YourChoice == 'P':
            print('You win !!')
        elif YourChoice == 's' or YourChoice == 'S':
            print('You lose !!')
        else:
            print("Invalid Choice... Choose between Rock(r or R) Paper(p or P) Scissor(s or S) !!")

    elif CompChoice == 'p':
        if YourChoice == 'p'or YourChoice == 'P':
            print("Tie")
        elif YourChoice == 's' or YourChoice == 'S':
            print('You win !!')
        elif YourChoice == 'r' or YourChoice == 'R':
            print('You lose !!')
        else:
            print("Invalid Choice... Choose between Rock(r or R) Paper(p or P) Scissor(s or S) !!")

    elif CompChoice == 's':
        if YourChoice == 's'or YourChoice == 'S':
            print("Tie")
        elif YourChoice == 'r' or YourChoice == 'R':
            print('You win !!')
        elif YourChoice == 'p' or YourChoice == 'P':
            print('You lose !!')
        else:
            print("Invalid Choice... Choose between Rock(r or R) Paper(p or P) Scissor(s or S) !!")


print('************************************')
print('Computer choose : ', CompChoice)
print('You choose : ', YourChoice)
print('************************************')
match = game(CompChoice, YourChoice)

