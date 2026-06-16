import matplotlib.pyplot as plt
import csv

xpoints = []
ypoints = []
with open('hasse.csv', 'r') as file:
    reader_obj = csv.reader(file)
    for row in reader_obj:
        xpoints.append(int(row[0]))
        xpoints.append(int(row[0]))
        ypoints.append(int(row[1]))
        ypoints.append(int(row[2]))
plt.plot(xpoints, ypoints, 'o')
plt.xlabel("prime")
plt.ylabel("Hasse bound")
plt.savefig("hasse.png")

