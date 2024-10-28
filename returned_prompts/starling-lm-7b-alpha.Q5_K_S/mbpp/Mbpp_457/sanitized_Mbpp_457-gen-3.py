def Find_Min(l):
    min_length = len(l[0])
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    for i in range(len(l)):
        if len(l[i]) == min_length:
            return l[i]