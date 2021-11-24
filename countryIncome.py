import library 

playerData = library.loadList("playerInfo.csv")
countryData = library.loadList("countryInfo.csv")
earningsData = []

for n in range(0, len(countryData)):
    totalEarnings = 0 
    countryCode = countryData[n][3].lower()
    playerCount = 0 
    for p in range (0, len(playerData)):
        #print(countryCode, playerData[p][4])
        if countryCode == playerData[p][4]:
            totalEarnings += float(playerData[p][5])
            playerCount += 1
    if playerCount > 0: 
        countryAverage =  totalEarnings/playerCount
        earningsData += [[countryData[n][2], totalEarnings, playerCount, countryAverage]]

for n in earningsData:
    print (n)
