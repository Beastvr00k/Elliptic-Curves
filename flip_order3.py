import csv
import pandas as pd
from sage.all import next_prime, previous_prime
flip_num = pd.read_csv('prime_elliptic_order.csv', header=None, names=['a', 'b', 'prime', 'order'])
order_loop = []

def find_order_range(prime, arr):
    if(prime == 2):
        prime_before = 2 
    else:
        prime_before = previous_prime(prime)
    prime_after = next_prime(prime)
    low, high = 0, len(arr) - 1
    lower_bound = -1
    while low <= high:
        mid = (low + high) // 2
        if arr.iat[mid, 2] <= prime_before:
            lower_bound = mid
            low = mid + 1
        else:
            high = mid - 1

    # ---- Find upper_bound: first index where arr[i][2] >= prime_after ----
    low, high = 0, len(arr) - 1
    upper_bound = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr.iat[mid, 2] >= prime_after:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1

    return lower_bound + 1, upper_bound - 1

def find_a_range(a_val, arr, lower_index, upper_index):
    low, high = lower_index, upper_index
    lower_bound = -1
    while low <= high:
        mid = (low + high) // 2
        if arr.iat[mid, 0] <= a_val - 1:
            lower_bound = mid
            low = mid + 1
        else:
            high = mid - 1

    # ---- Find upper_bound: first index where arr[i][2] >= prime_after ----
    low, high = lower_index, upper_index
    upper_bound = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr.iat[mid, 0] >= a_val + 1:
            upper_bound = mid
            high = mid - 1
        else:
            low = mid + 1
    if(lower_bound <= upper_bound):
        return lower_bound + 1, upper_bound - 1 
    else:
        return -1

def find_b_range(b_val, arr, lower_index, upper_index):
    low, high = lower_index, upper_index
    while low <= high:
        mid = (low + high) // 2
        if(arr.iat[mid, 1] == b_val):
            return mid
        if arr.iat[mid, 1] < b_val:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def find_index(a_val, b_val, arr, prime):
    if(prime < 5 or prime > 353):
        return -1
    if(a_val >= prime or b_val >= prime):
        return -1
    lower_bound, upper_bound = find_order_range(prime, arr)
    less_bound, high_bound = find_a_range(a_val, arr, lower_bound, upper_bound)
    return find_b_range(b_val, arr, less_bound, high_bound)


for i in range(0, len(flip_num)):
    array_path = []
    a = flip_num.iat[i, 0]
    b = flip_num.iat[i, 1]
    prime = flip_num.iat[i, 2]
    array_path.append(prime)
    order = flip_num.iat[i, 3]
    ind = find_index(a, b, flip_num, order)
    if(ind != -1 and order > prime):
        if(flip_num.iat[ind, 3] == prime):
            order_loop.append([a, b, prime, order])
            print([a, b, prime, order])


with open('flip_order.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(order_loop)

