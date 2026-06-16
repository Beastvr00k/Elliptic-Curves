import csv
from sage.all import is_prime
prime_val = []
with open('elliptic_order.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        if(is_prime(lines[3])):
            prime_val.append(lines)
            print(lines)
with open('prime_elliptic_order.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(prime_val)
