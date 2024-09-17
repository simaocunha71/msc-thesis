
def index_multiplication(tup1,tup2):
    return tuple(tuple(i*j for i,j in zip(tup1[i],tup2[i])) for i in range(len(tup1)))


