def index_multiplication(t1, t2):
    result = ()
    for i in range(len(t1)):
        result += ((t1[i][0] * t2[i][0], t1[i][1] * t2[i][1]),)
    return result