def tuple_modulo(t1, t2):
    t3 = []
    for i in range(len(t1)):
        t3.append(t1[i] % t2[i])
    return tuple(t3)


"""
Write a function which takes two tuples of the same length and performs the element wise multiplication.
assert tuple_multiply((3, 2, 5, 7), (8, 7, 4, 3)) == (24, 14, 20, 21)
"""

def tuple_multiply(t1, t2):
    t3 = []
    for i in range(len(t1)):
        t3.append(t1[i] * t2[i])
    return tuple(t3)

"""
Write a function which takes two tuples of the same length and performs the element wise addition.
assert tuple_add((10, 4, 5, 6), (5, 6, 7, 5)) == (15, 10, 12, 11)
"""

def tuple_add(t1, t2):
    t3 = []
    for i in range(len(t1)):
        t3.append(t1[i] + t2[i])
    return tuple(t3)

"""
Write a function which takes a tuple and a number n and returns the nth element of the tuple.
assert tuple_element(('a', 'b', 'c', 'd'), 2) == 'c'
"""
def tuple_element(t, n):
    return t[n]

"""
Write a function which takes a tuple and returns a new tuple which contains all the elements of the original tuple in reverse order.
assert tuple_reverse(('a', 'b', 'c', 'd')) == ('d', 'c', 'b', 'a')
"""

def tuple_reverse(t):
    return tuple(t[::-1])

"""
Write a function which takes a tuple and a number n and replaces the nth element of the tuple with the value of the number.
assert tuple_replace((1, 2, 