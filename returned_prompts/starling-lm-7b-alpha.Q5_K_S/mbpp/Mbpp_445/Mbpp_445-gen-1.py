from functools import reduce
def index_multiplication(t1,t2):
    t1_len = len(t1)
    t2_len = len(t2)
    assert t1_len==t2_len
    result = []
    for i in range(t1_len):
        result.append((t1[i]*t2[i],))
    return tuple(result)

"""
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)))

"""
assert index_multiplication((1,2,3),(4,5,6)) == (4, 10, 18)
"""
index_multiplication((1,2,3),(4,5,6))

"""
assert index_multiplication((1),(2)) == (2,)
"""
index_multiplication((1),(2))

"""
assert index_multiplication(((1, 3),),((6, 7))) == (6, 7)
"""
index_multiplication(((1, 3),),((6, 7)))

"""
assert index_multiplication(((1, 3), (4, 5)),((6, 7), (3, 9), (1, 1))) == ((6, 21), (12, 45), (3, 3))
"""
index_multiplication(((1, 3), (4, 5)),((6, 7), (3, 9), (1, 1)))

"""
assert index_multiplication(((1, 3), (4, 5)),((6, 7))) == ((6, 21), (