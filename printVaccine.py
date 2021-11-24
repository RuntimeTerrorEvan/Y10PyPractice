import csv

def loadList(fileName):
    with open(fileName, newline = '') as csv_file:
        reader = csv.reader(csv_file)
        dataList = list(reader)
    return dataList               

    #main
myData = loadList('asteroids.csv')    

for i in myData:
        print(i)           

for i in range (0, len(myData)):    
    print(myData[i])       

#for i in range (0,10):
#   print(myData[i][0])              
# Prints the first column                                                                                            