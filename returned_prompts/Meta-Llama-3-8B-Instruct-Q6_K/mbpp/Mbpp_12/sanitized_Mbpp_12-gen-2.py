from functools import reduce
import operator
def sort_matrix(matrix):
    return [list(t) for t in sorted(zip(*map(sorted, matrix)), key=sum)]