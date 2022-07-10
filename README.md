# python-random-game
python random number game

This is python code which generate random numbers from 1 to 6 we want to guess the correct number from 1 to 6 .
if we guess the correct number first time then we get 20 as our score . if we guess wrong number then our score will be decremented by 1.

For simplicity iam using 1 to 6 you can  use any numbers  as you wish in " random.randint(1 ,600)"

here iam using termcolor module for printing coloured text on the terminal. import termcolor in this manner " from termcolor import colored"
To print colored text use in this manner " print(colored("HELLO WORLD !","your colour name"))"

Here iam importing "random" module.

random module is used to generate random numbers.

Here we are using two while loops. first while loop for generating random number and taking decision of the user whether user want to play game or not.
if user enter "yes" the game will start from beginning . if user enters "no" then game stops.

second while loop is used to take input from the user .here user want to enter the correct number here we are using "if statement" to check the input of the user
if user enters correct number then we will print entered number is correct and we break the if statement and print the score.
if user enters wrong number then we go to the "else" block and print guess the number.... and continue the second while loop 

second while loop stops only if  user enters correct number or guess the correct number.
