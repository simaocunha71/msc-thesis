def find_length(s):
    max_diff = 0
    count_0s = 0
    count_1s = 0

    for c in s:
        if c == '0':
            count_0s += 1
        else:
            count_1s += 1

        max_diff = max(max_diff, abs(count_0s - count_1s))

    return max_diff