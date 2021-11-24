#Determine if a number is even
def isEven(num):
    result = False
    if num % 2 ==0:
        result = True 
    return result
# return (num %2)

#Function that gets 2 numbers and returns the smallest of the two 
def getSmallest(num1, num2):
    small = num1
    if num2 < num1:
        small = num2 
    return small




