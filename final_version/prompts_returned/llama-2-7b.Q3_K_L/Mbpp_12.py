"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

class Solution(object):
    def sortMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        col = []
        for i in range (len(matrix)):
            max_i = 0
            
            for j in range (1, len(matrix[0])):
                if matrix[i][j] > matrix[max_i][j]:
                    max_i = i
                    
                elif matrix[i][j] == matrix[max_i][j]:
                    pass
            
            col.append(max_i)
        
        res = []
        for row in range (len(matrix)):
            if len(col) - 1 < row:
                continue
            
            res.append(sum([int(matrix[row][j]) for j in range (len(matrix[0]))]))
        
        return sorted(res, reverse=True)