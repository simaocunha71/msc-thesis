def find_length(s):
    max_diff = 0
    count_zero = 0
    count_one = 0
    for char in s:
        if char == '0':
            count_zero += 1
            max_diff = max(max_diff, count_one - count_zero)
        else:
            count_one += 1
            max_diff = max(max_diff, count_one - count_zero)
    return max_diff