from math import comb
def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum([comb(n-1, k-1)*bell_number(k-1) for k in range(1, n+1)])