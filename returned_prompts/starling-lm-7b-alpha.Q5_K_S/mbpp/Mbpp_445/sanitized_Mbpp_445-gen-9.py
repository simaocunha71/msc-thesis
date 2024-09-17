def index_multiplication(t1,t2):
    l = []
    for i in range(len(t1)):
        l.append((t1[i]*t2[i]))
    return tuple(l)