import random
from termcolor import colored

while True:
    ran = random.randint(1,6)
    count = 20
    while True:
        user = int(input("enter the number:"))
        if user == ran:
            print(colored(f"YOUR NUMBER IS CORRECT {ran}","blue"))
            break
        else:
            print(colored("GUESS the number.....","red"))
            count=count-1
            continue
    print("YOUR SCORE : ",count)
    users = input("DO YOU WANT TO PLAY AGAIN yes/no :")
    if users == "yes":
        continue
    else:
        break    