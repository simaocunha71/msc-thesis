"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
from typing import List

def max_of_nth(matrix:List, n=0):
    """
    return the max of the i'th row in a matrix, i.e. the max value along an axis
    """
    if not isinstance(matrix, list):
        raise TypeError("'max_of_nth': matrix must be a list")
    
    if n < 0:
        return 0
        
    # check that we are dealing with a square matrix; we do this by checking that the length of
    # the matrix is equal to its width. if it isn't, raise an error and return None as there is no valid solution
    if len(matrix) != len(matrix[0]):
        raise ValueError("'max_of_nth': matrix must be square")
    
    num_elements = len(matrix)
    # we use a nested for loop to iterate along the row dimension of the matrix
    max_element:int = None
    # keep track of which index in the iterated list belongs to a particular row
    current_index=0
    
    if n < num_elements:  # check that n is between 0 and num_elements
        for i in range(n,num_elements): # iterate through each row starting at (n+1) and ending one less than the matrix size minus 1
            
            current_row = matrix[i]    # get a list of all elements belonging to this particular row
            
            if max_element is None:  # check that we are dealing with a valid matrix, i.e., we don't have any invalid input
                max_element=max(current_row) # find the max element in our current row and store it as max_element
                        
            else:
                if max_element > max(current_row):  # check that our current row has an element greater than or equal to our previous max
                    max_element=max(current_row)  # update max_element with the max from the new row, if applicable
        
            # store which index in the iterated list belongs to a particular row. this will be used to retrieve the relevant element when updating max_element
            current_index = i
    else:
        raise IndexError("'