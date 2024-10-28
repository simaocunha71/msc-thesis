def sort_matrix(matrix):
    return [list(t) for t in sorted(zip(*matrix), key=sum)]