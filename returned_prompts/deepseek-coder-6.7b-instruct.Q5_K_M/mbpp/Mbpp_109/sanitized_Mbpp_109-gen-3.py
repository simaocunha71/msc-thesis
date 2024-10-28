def odd_Equivalent(bin_str, rotations):
    odd_count = 0
    bin_str = bin_str * rotations
    for i in range(rotations):
        rotated_str = bin_str[i:len(bin_str) - rotations + i] + bin_str[0:i]
        if int(rotated_str, 2) % 2 != 0:
            odd_count += 1
    return odd_count