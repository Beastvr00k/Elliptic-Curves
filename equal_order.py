import csv
equal_val = []
with open('elliptic_order.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        if(lines[2] == lines[3]):
            equal_val.append(lines)
            print(lines)
with open('equal_elliptic_order.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(equal_val)