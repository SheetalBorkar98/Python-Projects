
import random

randno = random.randint(1,100)

user = None
count = 0

while (user != randno):
    try:
        user = int(input("\nGuess the number computer might have choosed (Press 0 to quit playing) : "))

        if user == 0:
            print("\nQuitting game...\n")
            break
        else:
            if user > randno:
                print("\nPlease choose a lower number..")
                count += 1
            elif user < randno and user >0:
                print("\nPlease Choose a bigger number..")
                count += 1
            else:
                count += 1

    except Exception as e:
        print("\nEnter a valid integer...")

if user == 0:
    pass
else:
    print("\nComputer choose : ",randno)
    print(f"\nYou guessed the correct number after {count} trails")
