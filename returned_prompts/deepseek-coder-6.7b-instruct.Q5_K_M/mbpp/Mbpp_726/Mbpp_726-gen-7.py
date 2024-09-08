def multiply_elements(t):
    return tuple([t[i]*t[i+1] for i in range(len(t)-1)])

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# OR

def multiply_elements(t):
    return tuple(map(lambda x, y: x*y, t[:-1], t[1:]))

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# OR

def multiply_elements(t):
    return tuple(a*b for a, b in zip(t, t[1:]))

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# OR

def multiply_elements(t):
    return tuple(starmap(lambda x, y: x*y, zip(t, t[1:])))

from itertools import starmap

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# OR

def multiply_elements(t):
    return tuple(reduce(lambda x, y: (x[0]*y, ) + x[1], enumerate(t[1:], 1), (1, ))[1])

from functools import reduce

print(multiply_elements((1, 5, 7, 8, 10)))  # (5, 35, 56, 80)

# OR

def multiply_elements(t):
    return tuple(x*y for x, y in pairwise(t))

from itertools import tee, islice

def pairwise(iterable):
    a, b = tee(iterable)
    _ = next(b