import math
def armstrong_number(n):
    num_str = str(n)
    length = len(num_str)
    sum = 0
    for i in num_str:
        sum += int(i) ** length
    if sum == n:
        return True
    else:
        return False