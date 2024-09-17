from math import factorial as f
def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sum(f(n + k - 1) / (n + k - 1) / f(n) / f(k) for k in range(n + 1))