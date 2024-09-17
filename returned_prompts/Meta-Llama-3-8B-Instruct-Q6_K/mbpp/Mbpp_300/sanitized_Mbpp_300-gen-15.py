def count_binary_seq(n):
    total = 0
    for i in range(2**n):
        bin_str = bin(i)[2:].zfill(n)
        if sum(int(digit) for digit in bin_str) == sum(int(digit) for digit in bin_str[::-1]):
            total += 1
    return total