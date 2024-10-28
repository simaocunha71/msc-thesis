from math import comb
def count_binary_seq(n: int) -> float:
    total = 0.0
    for i in range(2**n):
        bits = bin(i)[2:]
        bits = bits.zfill(2*n)
        first_half = sum(int(digit) for digit in bits[:n])
        second_half = sum(int(digit) for digit in bits[n:])
        if first_half == second_half:
            total += 1
    return total