def find_length(s):
    max_diff = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j].count('0') > s[i:j].count('1'):
                max_diff = max(max_diff, s[i:j].count('0') - s[i:j].count('1'))
            else:
                max_diff = max(max_diff, s[i:j].count('1') - s[i:j].count('0'))
    return max_diff