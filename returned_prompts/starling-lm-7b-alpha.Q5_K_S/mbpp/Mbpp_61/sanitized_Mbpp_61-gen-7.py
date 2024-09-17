def count_Substrings(s):
    res = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            tmp = 0
            for x in s[i:j+1]:
                tmp += int(x)
            if tmp == j-i+1:
                res += 1
    return res