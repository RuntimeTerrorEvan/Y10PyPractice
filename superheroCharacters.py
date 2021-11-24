from library import loadList

categories = {"name":1, "good":4, "sex":7, "identity":3}

dc= loadList("dcSuperheros.csv")
marvel = loadList("marvelSuperheros.csv")

universe = dc + marvel 

for n in range (0, len(universe)):      
    if (universe[n][categories["good"]] == "Good Characters",universe[n][categories["sex"]] == "Female Characters" ):
        print(universe[n][categories["name"]], "  ,  ", universe[n][categories["identity"]])
 








