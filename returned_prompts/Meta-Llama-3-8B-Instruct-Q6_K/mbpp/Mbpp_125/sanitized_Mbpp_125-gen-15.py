def find_length(s):
    max_diff = 0
    curr_diff = 0
    zeros = 0
    ones = 0
    for char in s:
        if char == '0':
            zeros += 1
        else:
            ones += 1
        curr_diff = abs(zeros - ones)
        max_diff = max(max_diff, curr_diff)
    return max_diff