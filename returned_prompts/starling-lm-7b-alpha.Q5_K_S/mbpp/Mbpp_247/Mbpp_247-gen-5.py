
def lps(s):
    lengths = [0] * len(s)
    lengths[0] = 1
    for i in range(len(s)):
        for j in range(i):
            if s[i] == s[j]:
                lengths[i + 1] = max(lengths[i + 1], lengths[j] + 1)
    return lengths[-1]


