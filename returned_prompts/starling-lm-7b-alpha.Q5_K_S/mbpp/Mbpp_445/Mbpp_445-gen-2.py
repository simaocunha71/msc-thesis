def index_multiplication(t1,t2):
    t3 = []
    for i in range(len(t1)):
        t3.append((t1[i]*t2[i],))
    return tuple(t3)

# Test
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))

# Another approach
def index_multiplication_alt(t1,t2):
    return tuple(list(map(lambda x: x[0]*x[1], zip(t1,t2))))

# Test
assert index_multiplication_alt(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))

"""
The function index_multiplication(t1,t2) takes two tuples as input and performs index wise multiplication.
The function index_multiplication_alt(t1,t2) is an alternate approach to solve the problem and is faster since it uses map and zip functions.

"""

# Performance comparison
import timeit

def measure_performance(func, *args):
    start = timeit.default_timer()
    func(*args)
    end = timeit.default_timer()
    return end - start

# Test performance
print(measure_performance(index_multiplication,((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))))
print(measure_performance(index_multiplication_alt,((1, 3), (4, 5), (2, 9), (1, 