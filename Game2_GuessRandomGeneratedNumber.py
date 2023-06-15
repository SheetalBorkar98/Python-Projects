
import random

randno = random.randint(1,100)
print(randno)
user = None
count = 0

while (user != randno):
    try:
        user = int(input("Guess which number the computer might have choosed : "))
        if user > randno:
            print("Please choose a lower number..")
            count += 1
        elif user < randno:
            print("Please Choose a bigger number..")
            count += 1
        else:
            count += 1

    except Exception as e:
        print("Enter a valid integer...")


print(f"You guessed the correct number after {count} trails")
print("Computer choose : ",randno)