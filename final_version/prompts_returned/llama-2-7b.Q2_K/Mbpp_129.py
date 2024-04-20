"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""

def magic_square(matrix):
    """Check if matrix is a square"""
    if len(matrix) <= 1:
        print("You have to give more than one number")
        return False
    
    for i in range(0,len(matrix)):
        for j in range (0,len(matrix[0])):
            if matrix [i][j] == matrix [j][i]:
                continue
            else:
                break  #exit the loop as soon as a value is not same as its corresponding element
    return True if len(matrix) > 1 else False