def odd_Equivalent(bin_str, rotations):
    n = len(bin_str)
    bin_str = bin_str + bin_str
    odd_count = 0

    for i in range(rotations):
        odd_count += bin_str[i:n+i].count('1')

    return odd_count