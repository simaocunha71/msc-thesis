def count_binary_seq(n):
    total = 0
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)
        if sum(int(b) for b in binary[:n]) == sum(int(b) for b in binary[n:]):
            total += 1
    return total