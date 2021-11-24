import matplotlib.pyplot as plt

print("")
file = open("nasa.csv")
next(file)
for line in file:
    values = line.split(",", 5)
    minDia = float(values[3])
    maxDia = float(values[4])
    plt.scatter(minDia, maxDia, color = 'yellow')

plt.show()

