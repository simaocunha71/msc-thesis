"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
from typing import List
def max_of_nth(matrix:List[List[int]], col_index: int = 0)->int:
    """write your function definition here"""!
    if len(matrix) <= 0 or len(col_index) <= 0 or matrix[len(matrix)-1][len(col_index)-1] < 1:
        return -1
    else:
        col = 0; index = 0
        for i in range(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)):
            if matrix[i][col] < matrix[col][len(col)-1]:
                col = i + 1; index += 1
        return max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], col)
