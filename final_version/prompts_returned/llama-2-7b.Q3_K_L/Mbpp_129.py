"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
class Solution:
    def isMagicSquare(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        l = len(matrix)
        for i in range(1,l+1):
            a=sum(matrix[:i])
            b=sum(matrix[-i:])
            if abs(a-b) == i:
                return False