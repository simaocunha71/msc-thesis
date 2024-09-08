
def maximize_elements(t1, t2):
    res = ()
    for i in range(len(t1)):
        res += (max(t1[i][0], t2[i][0]), max(t1[i][1], t2[i][1])),
    return res

print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))

# Solution 2: Using list comprehension

def maximize_elements(t1, t2):
    return tuple(max(x) for x in zip(t1, t2))

print(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))))

"""
