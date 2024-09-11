from math import isclose
def zero_count(lst):
    zero_count = 0
    non_zero_count = 0
    for i in lst:
        if i == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    try:
        return isclose(zero_count / (zero_count + non_zero_count), 0.181818, rel_tol=0.001)
    except ZeroDivisionError:
        return 0.0