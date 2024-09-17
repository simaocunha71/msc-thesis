def index_multiplication(t1,t2):
    zipped = zip(t1,t2)
    return tuple(map(lambda x,y:x*y,zipped))