def lps(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    else:
        lps_length = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == s[0]:
                lps_length[i] = 1
        for i in range(1,len(s)):
            for j in range(i):
                if s[i] == s[j] and i - j + 1 > lps_length[i]:
                    lps_length[i] = i - j + 1
        return max(lps_length)