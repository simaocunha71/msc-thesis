def find_length(s):
    max_diff = 0
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
        max_diff = max(max_diff, abs(zeros - ones))
    return max_diff