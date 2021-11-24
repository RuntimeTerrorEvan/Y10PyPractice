#Find all given divisors of a a number
#Print as a list at the end

factors = []
(userNum) = int(input ("Please enter an integer"))
for x in range (1,userNum):
    if userNum % x == 0:
        factors.append(x)
print(factors)
      




