def find_length(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            zeros = s[i:j].count('0')
            ones = s[i:j].count('1')
            length = max(zeros, ones) - min(zeros, ones)
            max_length = max(max_length, length)
    return max_length