def find_length(s):
    max_diff = 0
    count0 = 0
    count1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1
        max_diff = max(max_diff, abs(count0 - count1))
    return max_diff