    s = s.split()
    s1 = s[0].split(" ")
    s1 = [int(i) for i in s1]
    s2 = s[1].split(" ")
    s2 = [int(i) for i in s2]
    return n - sum(s1) - sum(s2)


