from sage.all import Primes, EllipticCurve, GF
import csv
P = Primes()
def random_order(lower_prime, upper_prime):
    with open('equal_elliptic_order.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(lower_prime, upper_prime):
            if(i in P):
                for a_val in range(i):
                    for b_val in range(i):
                        if(not((4 * a_val ** 3 + 27 * b_val ** 2)) % i == 0):
                            order = EllipticCurve(GF(i), [a_val, b_val]).cardinality()
                            if(order == i):
                                print(f"x^3 + {a_val}x + {b_val} mod {i} has order {order}")
                                writer.writerow([a_val, b_val, i, order])
random_order(228, 300)