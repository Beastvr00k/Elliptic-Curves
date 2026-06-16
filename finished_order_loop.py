import csv
finished_loop = []
with open('finished_order_loop.csv', 'r', newline='') as csvfile:
    reader_obj = csv.reader(csvfile)
    for row in reader_obj: 
        if(row[2] != "1" and row[2] != "2"):
            finished_loop.append(row)
            print(row)

with open('long_finished_order_loop.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(finished_loop)
