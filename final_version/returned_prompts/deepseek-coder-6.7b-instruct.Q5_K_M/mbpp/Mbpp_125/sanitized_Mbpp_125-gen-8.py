def find_length(bin_str):
    max_diff = 0
    count_zero = 0
    count_one = 0

    for char in bin_str:
        if char == '0':
            count_zero += 1
        else:
            count_one += 1
        diff = count_one - count_zero
        if diff > max_diff:
            max_diff = diff
    return max_diff