import csv
import matplotlib.pyplot as plt
prime_val = []
prime_val.append(5)
prime_occurence = []
prime_occurence.append(0)
with open('prime_elliptic_order.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        if(int(lines[2]) != prime_val[-1]):
            prime_val.append(int(lines[2]))
            prime_occurence.append(1)
        else:
            prime_occurence[-1] += 1
prime_prob = []
for i in range(len(prime_occurence)):
    prime_prob.append(prime_occurence[i] / (prime_val[i] ** 2))

plt.plot(prime_val, prime_prob, 'o')
plt.xlabel("Prime")
plt.ylabel("Proportion with prime order")
plt.savefig("Prime_Prop.png")

