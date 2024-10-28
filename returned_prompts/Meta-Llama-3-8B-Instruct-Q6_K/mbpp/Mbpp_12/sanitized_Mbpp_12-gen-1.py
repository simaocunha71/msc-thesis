from functools import reduce
from operator import add
def sort_matrix(matrix):
    return [list(t) for t in sorted(enumerate(map(sum, matrix)), key=lambda x: x[1])]