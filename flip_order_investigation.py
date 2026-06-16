import csv
prime_order_count = []
with open('flip_order.csv', 'r') as file:
    reader_obj = csv.reader(file)
    for row in reader_obj:
        in_array = False
        for i in range(0, len(prime_order_count)):
            if((int)(row[2]) == prime_order_count[i][0] and (int)(row[3]) == prime_order_count[i][1]):
                prime_order_count[i][2] += 1
                in_array = True
        if(not in_array):
            prime_order_count.append([(int)(row[2]), (int)(row[3]), 1])

with open('prime_order_count.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(prime_order_count)


