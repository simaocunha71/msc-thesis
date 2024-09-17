def find_length(s):
    max_diff = 0
    diff = 0
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
        diff = abs(zeros - ones)
        max_diff = max(max_diff, diff)
    return max_diff