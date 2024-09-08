def odd_Equivalent(bin_str, rotations):
    n = len(bin_str)
    bin_str = bin_str + bin_str
    rotated_bin_str = [bin_str[i:i+n] for i in range(n)]
    for i in range(rotations):
        rotated_bin_str.append(rotated_bin_str.pop(0))
    odd_count = 0
    for bin_str in rotated_bin_str:
        if int(bin_str,2) % 2 != 0:
            odd_count += 1
    return odd_count