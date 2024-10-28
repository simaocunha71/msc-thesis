    n = int(n)
    s = s.split(" ")
    apples = int(s[0][2:])
    oranges = int(s[1][0:len(s[1])-1])
    mangos = n - (apples + oranges)
    return mangos


