

def sort_matrix(matrix):
    return [matrix[i] for i in sorted(range(len(matrix)), key=lambda x: sum(matrix[x]))]



