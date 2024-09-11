def sort_matrix(matrix):
    return [list(t) for t in sorted(zip(*map(lambda x: list(x), matrix)), key=sum)]