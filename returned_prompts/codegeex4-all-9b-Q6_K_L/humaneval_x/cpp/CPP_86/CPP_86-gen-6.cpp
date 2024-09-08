def anti_shuffle(s):
    if len(s)<1:
        return s
    s=s.split()
    for i in range(len(s)):
        s[i