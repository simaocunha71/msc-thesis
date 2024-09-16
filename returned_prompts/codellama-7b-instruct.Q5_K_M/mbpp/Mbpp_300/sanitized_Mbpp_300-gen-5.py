def count_binary_seq(n):
    count = 0
    for i in range(2**(2*n)):
        binary_seq = bin(i)[2:]
        if binary_seq[:n] == binary_seq[n:]:
            count += 1
    return count