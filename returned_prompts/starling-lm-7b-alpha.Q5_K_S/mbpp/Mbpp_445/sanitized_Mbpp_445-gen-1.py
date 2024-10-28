from functools import reduce
def index_multiplication(t1,t2):
    t1_len = len(t1)
    t2_len = len(t2)
    assert t1_len==t2_len
    result = []
    for i in range(t1_len):
        result.append((t1[i]*t2[i],))
    return tuple(result)