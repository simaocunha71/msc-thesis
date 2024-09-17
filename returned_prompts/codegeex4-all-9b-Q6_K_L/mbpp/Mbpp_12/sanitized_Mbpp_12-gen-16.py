def sort_matrix(mat):
    for row in mat:
        row.sort()
    mat.sort(key=sum)
    return mat