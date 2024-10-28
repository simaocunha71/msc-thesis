def count_Substrings(s):
    n = len(s)
    res = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += int(s[j])
            if curr_sum == j - i + 1:
                res += 1
    return res