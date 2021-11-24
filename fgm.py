for n in range(0,len(data)):
    if float(data[n][col["fgm"]]) >=3.0:
        message = "Above Average"
else:
    message = "Below Average"
playerList += [[data[n]][col["name"]], data[n][col["fgm"]]], message

 
