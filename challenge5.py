#Problem Number 5 

#7 is the max. number of guesses because with 8+ guesses you can always determine the random number 
#For a number between 1-1000, 10 would be the correct maximum number of guesses 

import random 
ranNumber = int(random.randint(1,101))
print(ranNumber) # I used the random integer function for simplicity 

Userattempt = int(input("PLease guess an integer between 1 and 100"))

while Userattempt > ranNumber:
    print("Too high!") 
if Userattempt == ranNumber:
    print("Correct! Congratulations")
if Userattempt < ranNumber:
    print("Too low!")

