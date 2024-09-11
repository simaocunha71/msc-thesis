from itertools import product
def maximize_elements(t1, t2):
    max_t = [max(x, y) for x, y in zip(t1, t2)]
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == max_t[i] and t2[j] == max_t[j]:
                continue
            if t1[i] == max_t[j] and t2[j] == max_t[i]:
                max_t[i], max_t[j] = max_t[j], max_t[i]
    return max_t

# assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))


"""
def maximize_elements(t1, t2):
    max_t = [max(x, y) for x, y in zip(t1, t2)]
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == max_t[i] and t2[j] == max_t[j]:
                continue
            if t1[i] == max_t[j] and t2[j] == max_t[i]:
                max_t[i], max_t[j] = max_t[j], max_t[i]
    return max_t

assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""

# This code is contributed by Sanket We understand it.

# This code contributed by