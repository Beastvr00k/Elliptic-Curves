import csv
from sage.all import next_prime
from math import floor, ceil
hasse = []
current_val = 5
while(current_val <= 353):
    lower_bound = current_val + 1 - 2 * current_val ** 0.5
    lower_bound = ceil(lower_bound)
    upper_bound = current_val + 1 + 2 * current_val ** 0.5
    upper_bound = floor(upper_bound)
    hasse.append([current_val, lower_bound, upper_bound])
    print([current_val, lower_bound, upper_bound])
    current_val = next_prime(current_val)

with open('hasse.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(hasse)