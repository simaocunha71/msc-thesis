def find_length(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            cur_len = j - i
            zeros = 0
            ones = 0
            for k in range(i, j):
                if s[k] == '0':
                    zeros += 1
                else:
                    ones += 1
            max_len = max(max_len, max(zeros, ones))
    return max_len