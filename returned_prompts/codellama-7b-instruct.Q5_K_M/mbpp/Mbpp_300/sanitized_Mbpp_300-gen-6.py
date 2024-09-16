def count_binary_seq(n):
    count = 0
    for i in range(1<<n):
        if sum(bin(i)[2:].zfill(n)[::-1]) == sum(bin(i)[2:].zfill(n)):
            count += 1
    return count