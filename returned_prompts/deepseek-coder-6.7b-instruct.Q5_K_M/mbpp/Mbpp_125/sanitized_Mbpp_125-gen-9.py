def find_length(binary_string):
    chars = list(binary_string)
    max_diff = 0
    count_0 = 0
    count_1 = 0
    for char in chars:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        diff = count_1 - count_0
        if diff > max_diff:
            max_diff = diff
    return max_diff