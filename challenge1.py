#Problem Number 1 
import library matplotlib.pyplot as plt

money = float(input("Please enter an amount of money in cents"))
round(money, 2) 

toonieDivisor = money // 200 
loonieDivisor = money % 200 // 100 
quarterDivisor = money % 200 % 100 // 25
dimeDivisor = money % 200 % 100 % 25 // 10
pennyDivisor = dimeDivisor % 200 % 100 % 25 % 10 // 1

print("toonies:", int(toonieDivisor), "loonies:", int(loonieDivisor), "quarters:",int(quarterDivisor), "dimes:", int(dimeDivisor), "pennys:", int(pennyDivisor))
