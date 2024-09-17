
def magic_square_test(mat):
    # calculate sum of first row elements
    sum = sum(mat[0])
    # calculate sum of each column
    for i in range(len(mat)):
        col_sum = 0
        for j in range(len(mat[i])):
            col_sum += mat[j][i]
        if col_sum != sum:
            return False
    # calculate sum of each row
    for i in range(len(mat)):
        row_sum = 0
        row_sum += sum(mat[i])
        if row_sum != sum:
            return False
    # calculate sum of diagonals
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(len(mat)):
        diag_sum1 += mat[i][i]
        diag_sum2 += mat[i][len(mat)-1-i]
    if diag_sum1 != sum or diag_sum2 != sum:
        return False
    return True


