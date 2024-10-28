def Find_Min_Length(l):
    if l == []:
        return 0
    return min(len(i) for i in l)

