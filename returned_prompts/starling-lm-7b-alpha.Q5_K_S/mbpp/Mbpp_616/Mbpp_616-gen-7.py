def tuple_modulo(t1, t2):
    l1 = len(t1)
    l2 = len(t2)
    assert l1 == l2, "length of tuples should be same"
    res = []
    for i in range(l1):
        res.append(t1[i]%t2[i])
    return tuple(res)

# def tuple_modulo(t1, t2):
#     l1 = len(t1)
#     l2 = len(t2)
#     assert l1 == l2, "length of tuples should be same"
#     res = []
#     for i in range(l1):
#         res.append(t1[i]%t2[i])
#     return tuple(res)

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

"""
Output:
(0, 4, 5, 1)
"""
















































































"""

def tuple_modulo(t1, t2):
    l1 = len(t1)
    l2 = len(t2)
    assert l1 == l2, "length of tuples should be same"
    res = []
    for i in range(l1):
        res.append(t1[i]%t2[i])
    return tuple(res)

# def tuple_modulo(t1, t2):
#     l1 = len(t1)
#     l2 = len(t2)
#     assert l1 == l2, "length of tuples should be same"
#     res = []
#     for i in range(l1):
#         res.append(t1[i]%t2[i])
#     return tuple(