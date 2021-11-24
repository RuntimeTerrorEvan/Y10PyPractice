import csv

def loadList(fileName):
    with open(fileName, newline = '') as csv_file:
        reader = csv.reader(csv_file)
        dataList = list(reader)
    return dataList               

    #main
myData = loadList('vaccination-data.csv')    

for i in myData:
        print(i)           

for i in range (0, len(myData)):    
    print(myData[i])                                                                                                                       