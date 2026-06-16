import csv
import matplotlib.pyplot as plt
prime_val = []
prime_val_2 = []
prime_occurence = []
prime_occurence_2 = []
with open('flip_order.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        prime1 = int(lines[2])
        prime2 = int(lines[3])
        if(prime1 in prime_val):
            index = prime_val.index(prime1)
            prime_occurence[index] += 1
        else:
            if(prime1 % 4 == 1):
                prime_val.append(prime1)
                prime_occurence.append(1)
        if(prime1 in prime_val_2):
            index = prime_val_2.index(prime1)
            prime_occurence_2[index] += 1
        else:
            if(prime1 % 4 == 3):
                prime_val_2.append(prime1)
                prime_occurence_2.append(1)
        if(prime2 in prime_val):
            index = prime_val.index(prime2)
            prime_occurence[index] += 1
        else:
            if(prime2 % 4 == 1):
                prime_val.append(prime2)
                prime_occurence.append(1)
        if(prime2 in prime_val_2):
            index = prime_val_2.index(prime2)
            prime_occurence_2[index] += 1
        else:
            if(prime2 % 4 == 3):
                prime_val_2.append(prime2)
                prime_occurence_2.append(1)


plt.plot(prime_val, prime_occurence, 'o', color="red")
plt.plot(prime_val_2, prime_occurence_2, 'o')
plt.xlabel("Prime")
plt.ylabel("Number of pairs")
plt.savefig("prime_mod_4_equals_1_Flip_order.png")