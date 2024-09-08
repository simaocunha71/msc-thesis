def find_length(bin_str):
    max_diff = 0
    count_1s = 0
    count_0s = 0

    for bit in bin_str:
        if bit == '1':
            count_1s += 1
        else:
            count_0s += 1
        max_diff = max(max_diff, abs(count_1s - count_0s))

    return max_diff