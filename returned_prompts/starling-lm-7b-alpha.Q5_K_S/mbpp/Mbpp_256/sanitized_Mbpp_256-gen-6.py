from math import sqrt
def count_Primes_nums(x):
    if x < 2:
        return 0
    sqrt_x = int(sqrt(x))
    table = [True] * (sqrt_x + 1)
    table[0] = False
    table[1] = False
    for i in range(2, sqrt_x + 1):
        if table[i]:
            for j in range(i * i, sqrt_x + 1, i):
                table[j] = False
    return sum(table)