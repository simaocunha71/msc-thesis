def find_length(binary_string):
    max_diff = 0
    count_0s = 0
    count_1s = 0

    for bit in binary_string:
        if bit == '0':
            count_0s += 1
        else:
            count_1s += 1

        max_diff = max(max_diff, abs(count_0s - count_1s))

    return max_diff