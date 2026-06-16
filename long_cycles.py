import random
from sage.all import Primes, EllipticCurve, GF, next_prime
P = Primes()
import csv

def iterations(n):
    for i in range(n):
        random_number = random.randint(100000, 999999)
        random_prime = next_prime(random_number)
        random_a = random.randint(0, random_prime)
        random_b = random.randint(0, random_prime)
        is_prime = True
        check_list = False
        order_loop = []
        order_loop.append(random_prime)
        if((4 * random_a ** 3 + 27 * random_b ** 2) % random_prime == 0):
            is_prime = False
        while(is_prime):
            try:
                curve = EllipticCurve(GF(random_prime), [random_a, random_b])
                order = curve.cardinality()
            except Exception as e:
                print(f"Failed on a={random_a}, b={random_b}, p={random_prime}")
                print(e)
                break
            if(order in P):
                random_prime = order
                if((4 * random_a ** 3 + 27 * random_b ** 2) % random_prime == 0):
                    is_prime = False
                if(random_prime in order_loop):
                    check_list = True
                    is_prime = False
                else:
                    order_loop.append(random_prime)
            else:
                order_loop.append(order)
                is_prime = False
        if(check_list):
            print(random_a, random_b, order_loop)
            with open('long_cycles.csv', 'a', newline='') as csvfile: 
                writer = csv.writer(csvfile)
                row = [random_a, random_b, order_loop, len(order_loop),len(order_loop) - order_loop.index(order)]
                writer.writerow(row)

iterations(100000)
