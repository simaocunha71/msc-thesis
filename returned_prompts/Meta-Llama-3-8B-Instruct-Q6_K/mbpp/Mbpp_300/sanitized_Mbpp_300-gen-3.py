from math import comb
def count_binary_seq(n):
    total = 2 ** (2 * n)
    count = 0
    for i in range(2 ** n):
        bin_str = bin(i)[2:].zfill(n)
        if sum(int(c) for c in bin_str) == sum(int(c) for c in bin_str[::-1]):
            count += 1
    return count / total