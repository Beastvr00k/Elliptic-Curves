#from sage.all import next_prime, previous_prime
import csv
import pandas as pd
flip_num = pd.read_csv('prime_elliptic_order.csv', header=None, names=['a', 'b', 'prime', 'order'])
flip_array = []

def three_binary(a, b, order, arr):
  #Getting minimum and maximum indices of array elements with same order
  min_val = -1
  change = False
  max_val = len(arr) + 1
  frozen_index = -1
  min_index = 0
  max_index = len(arr)
  test_index = len(arr)//2
  while(max_index - min_index != 1):
    if(order < arr.iat[test_index, 2]):
      max_index = test_index
      frozen_index = max_index
    elif(order == arr.iat[test_index, 2]):
      max_index = test_index
      if(not change):
        test_index = (test_index + max_index)//2
        change = True
    else:
      min_index = test_index
    test_index = (max_index + min_index)//2
    if(test_index == len(arr) - 1):
      return -1
  if(arr.iat[test_index, 2] != order):
    test_index += 1
  min_val = test_index
  max_index = frozen_index
  min_index = test_index
  while(max_index - min_index != 1):
    if(order < arr.iat[test_index, 2]):
      max_index = test_index
    else:
      min_index = test_index
    test_index = (max_index + min_index)//2
  if(not(test_index + 1 == len(arr) or arr.iat[test_index + 1, 2] != order)):
    test_index += 1
  max_val = test_index

  #Getting minimum and maximum indices of array elements with same a
  frozen_index = max_index
  change = False
  min_val_2 = -1
  max_val_2 = len(arr) + 1
  min_index = min_val
  max_index = max_val + 1
  test_index = (min_index + max_index)//2
  while(max_index - min_index != 1):
    if(a < arr.iat[test_index, 0]):
      max_index = test_index
      frozen_index = max_index
    elif(a == arr.iat[test_index, 0]):
      max_index = test_index
      if(not change):
        frozen_index = max_index
        change = True
    else:
      min_index = test_index
    test_index = (max_index + min_index)//2
  if(arr.iat[test_index, 0] != a):
    test_index += 1
  min_val_2 = test_index
  max_index = frozen_index
  min_index = test_index
  while(max_index - min_index != 1):
    if(a < arr.iat[test_index, 0]):
      max_index = test_index
    else:
      min_index = test_index
    test_index = (max_index + min_index)//2
  if(not(test_index + 1 > max_val or arr.iat[test_index + 1, 0] != a)):
    test_index += 1
  max_val_2 = test_index
  #Comparing b values are correct
  true_index = -1
  for ind in range(min_val_2, max_val_2+1):
    if(arr.iat[ind, 1] == b):
      true_index = ind
  if(true_index != -1):
    return arr.iloc[true_index]
  else:
    return true_index
  
def find_point(a, b, order, arr):
  for i in range(0, len(arr)):
    if(a == arr.iat[i, 0] and b == arr.iat[i, 1] and order == arr.iat[i, 2]):
      return arr.iat[i, 3]
  return -1

for i in range(0, len(flip_num)):
  a = flip_num.iat[i, 0]
  b = flip_num.iat[i, 1]
  prime = flip_num.iat[i, 2]
  order = flip_num.iat[i, 3]
  if(prime >= order):
    if(find_point(a, b, order, flip_num) == prime):
      flip_array.append([a, b, prime, order])
      print(a, b, prime, order)

with open('flip_order.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(flip_array)