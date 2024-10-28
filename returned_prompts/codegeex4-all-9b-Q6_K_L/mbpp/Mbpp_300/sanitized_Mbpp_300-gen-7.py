def count_binary_seq(n):
    total = 0
    for i in range(2**n):
        binary_str = bin(i)[2:].zfill(2*n)
        if sum(int(bit) for bit in binary_str[:n]) == sum(int(bit) for bit in binary_str[n:]):
            total += 1
    return total