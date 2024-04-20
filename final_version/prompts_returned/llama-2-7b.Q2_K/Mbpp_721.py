"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
class Solution(object):
    def findMaximumAverage(self, matrix):
        """
        :param matirx: list of lists of size N * N
        :return avg of the max path (the sum of all costs) / length of the path.
        """
        if not len(matrix[0]):
            return float("inf")
        costs = [cost for row in matrix for cost in row]
        # Sort them ascending, for every element we will try to find a sequence that covers all of them
        costs = sorted(costs)
        if not len(costs):
            print "No element was found"
            return float("inf")
        
        def findMaxSequence(sequence, matrix):
            # If the sequence is empty, we can't have any path:
            assert len(sequence) <= 1 or len(matrix[0]) >= len(sequence)-1, \
                "Matrix doesn't contain enough elements to cover {}".format(".".join([str(i) for i in sequence]))
        
            # To each element in the sequence we assign the index of it within the matrix (so as row and column).
            next_element = 0
            
            # If we found a sequence so far that covers all costs, then return the max sum of element's cost covered. Else return None:
            if len(sequence) == 1 or any([cost[next_element] not in costs for next_element in range(len(matrix)) and cost[next_element] in costs for next_element in range(len(matrix)), 0 < len(sequence)]):
                return maxAverageOfSequence(sequence, matrix)
        
        def maxAverageOfSequence(sequence, matrix):
            # If the sequence is empty, we can't have any path:
            assert len(sequence) <= 1 or len(matrix[0]) >= len(sequence)-1, \
                "Matrix doesn't contain enough elements to cover {}".format(".".join([str(i) for i in sequence]))
            
            # To each element in the sequence we assign the index of it within the matrix (so as row and column).
            next_element = 0
                    
            # If we found a sequence so