def count_Substrings(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    n = len(s)
    res = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += int(s[j])
            if sum == j-i+1:
                res += 1
    return res