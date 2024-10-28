def find_length(s):
    max_length = 0
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros += 1
            ones = 0
        else:
            ones += 1
            zeros = 0
        max_length = max(max_length, abs(zeros - ones))
    return max_length