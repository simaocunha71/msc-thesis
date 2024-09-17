import timeit
def index_multiplication(t1,t2):
    t3 = []
    for i in range(len(t1)):
        t3.append((t1[i]*t2[i],))
    return tuple(t3)