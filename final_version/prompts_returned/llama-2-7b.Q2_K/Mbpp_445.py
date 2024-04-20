"""
Write a function to perform index wise multiplication of tuple elements in the given two tuples.
assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
"""
import operator

def index_multiplication(tuples):
    result = []
    first = tuples[0]
    for i, t in enumerate(tuples[1:], start=1):
        first += tuple((first[i],) + (t[i],))
    return result

if __name__ == "__main__":
    print("Given :", tuples[0][1:])
    print("Result :", index_multiplication(tuples[1:]))
