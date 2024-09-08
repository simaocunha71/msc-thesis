def find_length(s):
    max_diff = 0
    count_zero = 0
    count_one = 0
    for i in s:
        if i == '0':
            count_zero += 1
        else:
            count_one += 1
        diff = count_one - count_zero
        if diff > max_diff:
            max_diff = diff
    return max_diff