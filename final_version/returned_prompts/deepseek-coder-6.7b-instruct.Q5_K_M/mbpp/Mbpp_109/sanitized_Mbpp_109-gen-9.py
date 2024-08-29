def odd_Equivalent(bin_str, rotations):
    bin_str = bin_str * rotations
    total = 0

    for i in range(len(bin_str)):
        rotated = bin_str[i:] + bin_str[:i]
        xor_result = int(rotated, 2) ^ int(bin_str, 2)
        total += bin(xor_result).count('1')

    return total // 2