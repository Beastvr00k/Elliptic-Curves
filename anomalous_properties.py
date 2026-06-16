import csv
import matplotlib.pyplot as plt
import random
def get_data():
    row_added = []
    with open('equal_elliptic_order.csv', 'r', newline='') as csvfile:
        reader_obj = csv.reader(csvfile)
        for row in reader_obj: 
            a = row[0]
            b = row[1]
            a = (int)(a)
            b = (int)(b)
            discriminant = 4 * a ** 3 + 27 * b ** 2 
            j_invariant = 1728 * (4 * a ** 3) / discriminant
            discriminant *= -16
            row.append(discriminant)
            row.append(j_invariant)
            row_added.append(row)
    with open('anomalous_with_j_discriminant.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(row_added)

def plot_data():
    xpoints = []
    ypoints = []
    with open('anomalous_with_j_discriminant.csv', mode='r') as file:
        reader_obj = csv.reader(file)
        for row in reader_obj:
            xpoints.append(float(row[5]))
    plt.hist(xpoints)
    plt.xlabel("j_invariant")
    plt.savefig("anomalous_j_invariant.png")

def plot_all_data():
    discriminant_arr = []
    j_invariant_arr = []
    with open('elliptic_order.csv', 'r', newline='') as csvfile:
        reader_obj = csv.reader(csvfile)
        for row in reader_obj: 
            a = row[0]
            b = row[1]
            a = (int)(a)
            b = (int)(b)
            discriminant = 4 * a ** 3 + 27 * b ** 2 
            j_invariant = 1728 * (4 * a ** 3) / discriminant
            discriminant *= -16
            discriminant_arr.append(discriminant)
            j_invariant_arr.append(j_invariant)
    plt.figure()
    plt.hist(discriminant_arr)
    plt.xlabel("all_discriminant")
    plt.savefig("elliptic_discriminant.png") 
    plt.figure()
    plt.hist(j_invariant_arr)
    plt.xlabel("all_j_invariant")
    plt.savefig("elliptic_j_invariant.png")

plot_all_data()

        