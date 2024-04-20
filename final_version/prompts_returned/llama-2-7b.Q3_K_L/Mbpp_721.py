"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
import collections
class Solution:
    def findMaximumAverage(self, mat):
        sum_cost = sum(mat) # total cost of the entire matrix
        
        max_paths = collections.defaultdict(list)
        for i in range(len(mat)):
            for j in range(i+1, len(mat[0])): 
                if mat[i][j] - mat[j][i]: # check if the cell is occupied or not
                    continue
                self.helper_func(mat, i, j, max_paths)
            max_path = max(max_paths.items(), key=lambda x:x[1])[0]
        return sum_cost / len(max_path)  # average of max path is returned
    
    def helper_func(self, mat, i, j, max_paths):
        if (i,j) in max_paths or mat[i][j] == None:
            return
        
        # if the cell is occupied by a zero, means that this is not a path, so we skip it.
        max_paths[(i, j)] = self.helper_func(mat, i + 1, j, max_paths) - sum(mat[i:j+1])  
    """
    The complexity for the above function is `O(N^2)`
    
    If we want to minimize it further, we can implement a different version of helperFunc that takes into consideration two parameters (i-1, j) and (i+1, j), then we will have only one pass through the matrix. 
    """
