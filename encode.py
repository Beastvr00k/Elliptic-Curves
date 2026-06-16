from sage.crypto.util import ascii_integer
from sympy.functions import legendre
from sage.all import power_mod, BinaryStrings

def embedding(p, msg, a, b): #p is a prime, msg is a real word
    bin = BinaryStrings()
    if (p % 4 != 3):
        return None
    total = 0
    flip_msg = msg[::-1]
    for i in range(len(flip_msg)):
        binary_rep = bin.encoding(flip_msg[i])
        total += (256 ** i * ascii_integer(binary_rep))
    string_total = str(total)
    string_total_flip = string_total[::-1]
    valid_p = p // 1000 - 1
    running_num = 0
    running_power = 0
    output_array = []
    for i in range(0, len(string_total_flip)):
        if(running_num + int(string_total_flip[i]) * (10 ** running_power) < valid_p):
            running_num += int(string_total_flip[i]) * 10 ** running_power
            running_power += 1
        else:
            output_array.append(running_num)
            running_power = 1
            running_num = int(string_total_flip[i])
    output_array.append(running_num)
    output_array_flip = output_array[::-1]
    output_x_vals = []
    for element in output_array_flip:
        new_element = element * 1000
        break_val = False
        if(new_element == element * 1000 + 1000):
            break_val = True
            output_x_vals.append(None)
        while(not break_val):
            if(legendre(new_element ** 3 + a * new_element + b, p) == 1):
                break_val = True
                output_x_vals.append(new_element)
            else:
                new_element += 1
    output_y_vals = []
    for x_val in output_x_vals:
        func = (x_val ** 3 + a * x_val + b) % p
        func_power = power_mod(func, (p + 1)/4, p)
        output_y_vals.append(func_power)
    output_points = []
    for i in range(len(output_x_vals)):
        point = (output_x_vals[i], output_y_vals[i])
        output_points.append(point)
    return output_points
print(embedding(1236589502212421527, "today", 1, 34))