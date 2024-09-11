from itertools import zip_longest
def index_multiplication(t1,t2):
    return tuple(map(lambda x,y:x*y,t1,t2))



"""
def index_multiplication(t1,t2):
    zipped = zip(t1,t2)
    return tuple(map(lambda x,y:x*y,zipped))

"""



"""
def index_multiplication(t1,t2):
    return tuple(map(lambda x:tuple(map(lambda y:x*y,t1[i],t2[i])) for i in range(len(t1))))

"""


"""
def index_multiplication(t1,t2):
    t1_len = len(t1)
    t2_len = len(t2)
    multiplied_tuple = []
    for i in range(t1_len):
        multiplied_tuple.append(t1[i]*t2[i])
    return tuple(multiplied_tuple)

"""


def test_index_multiplication():
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))


test_index_multiplication()
"""


def index_multiplication(t1,t2):
    zipped_list = list(zip(t1,t2))
    return tuple(map(lambda x:(x[0]*x[1]),zipped_list))


def test_index_multiplication():
    assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 21), (12, 45), (2, 9), (7, 30))
