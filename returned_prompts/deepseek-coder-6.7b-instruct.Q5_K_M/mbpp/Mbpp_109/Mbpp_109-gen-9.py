
def odd_Equivalent(bin_str, rotations):
    odd_count = 0
    for i in range(rotations):
        bin_str = bin_str[1:] + bin_str[0]
        odd_count += bin_str.count('1')
    return odd_count


