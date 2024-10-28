def count_binary_seq(n):
    count = 0
    for i in range(2**n):
        if bin(i).count('1') == bin(i).count('1')[::-1].count('1'):
            count += 1
    return count