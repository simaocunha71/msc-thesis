    l.sort()
    for i in range(len(l)-2):
        a, b, c = l[i], l[i+1], l[i+2]
        if a + b + c == 0:
            return True
    return False


