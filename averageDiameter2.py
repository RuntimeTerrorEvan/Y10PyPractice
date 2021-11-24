from library import loadList

col = {"name":1, "minDi":3, "maxDi":4}
data = loadList("asteroids.csv")

    
averageDi = float((data[n][col["minDi"]] + data[n][col["maxDi"]])) / 2 

for n in range (0, len(data)):
    print(averageDi)


        