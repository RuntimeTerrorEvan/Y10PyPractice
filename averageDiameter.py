print("")
f = open("nasa.csv")
next(f)
for line in f:
    values = line.split(",", 5)
    minDia = float(values[3])
    maxDia = float(values[4])
    print((minDia + maxDia)/2)
    