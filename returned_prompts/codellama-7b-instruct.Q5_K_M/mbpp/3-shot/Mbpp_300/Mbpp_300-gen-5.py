
def count_binary_seq(n):
    count = 0
    for i in range(2**n):
        bin_str = bin(i)[2:]
        if len(bin_str) == n:
            if sum(list(map(int, bin_str[:n]))) == sum(list(map(int, bin_str[n:]))) :
                count += 1
    return count


