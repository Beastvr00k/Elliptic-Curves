import csv
import matplotlib.pyplot as plt
val = []
occurence = []
with open('flip_order.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        b = int(lines[1])
        b %= 5
        if(b in val):
            index = val.index(b)
            occurence[index] += 1
        else:
            val.append(b)
            occurence.append(1)


plt.plot(val, occurence, 'o')
plt.xlabel("b_val")
plt.ylabel("Number of pairs")
plt.savefig("b_mod_5_val_flip_order.png")