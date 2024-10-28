def index_multiplication(t1, t2):
    result = []
    for i in range(len(t1)):
        result.append(tuple(x*y for x,y in zip(t1[i],t2[i])))
    return tuple(result)