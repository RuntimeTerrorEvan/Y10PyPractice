from library import loadList

with open("nasa.csv") as f:
    next(f)
    minDia = [float(line.split(",", 5)[3]) for line in f if line]
    maxDia = [float(line.split(",", 5[4])) for line in f if line]

    print(minDia + maxDia)

    


#asteroids = loadList("nasa.csv")

#categories = {"minDia":3,"maxDia":4, "mph":14, "uncertainty":22}

#for n in range (0, len(asteroids)):  
    #asteroids.replace(".", ".")
    #print (FloatingPointError(asteroids[n][categories["minDia"]]) + FloatingPointError(asteroids[n][categories["maxDia"]]))
    

  # if (asteroids[n][categories["good"]] == "Good Characters",universe[n][categories["sex"]] == "Female Characters" )
#print(universe[n][categories["name"]], "  ,  ", universe[n][categories["identity"]]