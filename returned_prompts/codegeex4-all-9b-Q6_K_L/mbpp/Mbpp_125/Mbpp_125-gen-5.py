def find_length(binary_string):
    n = len(binary_string)
    max_diff = 0
    count_0 = 0
    count_1 = 0
    for i in range(n):
        if binary_string[i] == '0':
            count_0 += 1
        else:
            count_1 += 1
        max_diff = max(max_diff, abs(count_0 - count_1))
    return max_diff

