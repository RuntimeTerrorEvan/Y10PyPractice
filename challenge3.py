#Problem Number 3 
#Find all integer divisors of a given number 
#Print one at a time

(userNum) = int(input ("Please enter an integer"))
for x in range (1,userNum):
    if userNum % x == 0:
        print(x)
        








