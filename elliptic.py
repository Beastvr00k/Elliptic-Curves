from sage.all import EllipticCurve, GF, is_prime
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_with_order
from sage.plot.scatter_plot import scatter_plot
from matplotlib import pyplot as plt

def array_order(desired_order):
    it = EllipticCurve_with_order(desired_order)
    curve_array = []
    for curve in it:
        field_size = curve.base_field().order()
        if is_prime(field_size):
            curve_array.append(curve)
    return len(curve_array)

vals = []
nums = [i for i in range(2, 100)]
for i in nums:
    val = array_order(i)
    print("Number of curves of order " + str(i) + ": " + str(val))
    vals.append(val)
    
'''points = []
for j in range(0, len(nums)):
    points.append([nums[j], vals[j]])'''
plt.plot(nums, vals, 'cs')
plt.show()