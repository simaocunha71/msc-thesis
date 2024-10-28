def find_length(s):
    max_diff = 0
    count_zeros = 0
    count_ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            count_zeros += 1
        else:
            count_ones += 1
        max_diff = max(max_diff, abs(count_zeros - count_ones))
    return max_diff