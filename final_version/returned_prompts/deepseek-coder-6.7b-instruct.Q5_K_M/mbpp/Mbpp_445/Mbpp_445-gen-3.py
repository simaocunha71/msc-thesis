
def index_multiplication(tuples):
    t1, t2 = tuples
    res = []
    for i in range(len(t1)):
        res.append(tuple(map(lambda x, y: x*y, t1[i], t2[i])))
    return tuple(res)

print(index_multiplication((((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3)))))

# Output:
# ((6, 21), (12, 45), (2, 9), (7, 30))



