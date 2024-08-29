def digit_distance_nums(a, b):
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    if len_a != len_b:
        return "Invalid numbers"
    sum_diff = 0
    for i in range(len_a):
        sum_diff += abs(int(str_a[i]) - int(str_b[i]))
    return sum_diff

print(digit_distance_nums(1,2))  # returns 1


"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(123, 321) == 12
"""

def digit_distance_nums(a, b):
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    if len_a != len_b:
        return "Invalid numbers"
    sum_diff = 0
    for i in range(len_a):
        sum_diff += abs(int(str_a[i]) - int(str_b[i]))
    return sum_diff

print(digit_distance_nums(123, 321))  # returns 12


"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(111, 222) == 0
"""

def digit_distance_nums(a, b):
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    if len_a != len_b:
        return "Invalid numbers"
    sum_diff = 0
    for i in range(len_a):
        sum_diff += abs(int(str_a[i]) - int(str_b[i]))
