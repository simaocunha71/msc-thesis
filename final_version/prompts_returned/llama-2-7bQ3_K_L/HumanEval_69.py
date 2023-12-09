
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    
    if len(lst)==0: return -1
    result=0  # The result of the function. The result is not set here, and we'll make sure it's set later
    def helper(lst, index):
        '''Helper function to handle one element at a time'''    
        
        if (index==len(lst)): return -1
        if lst[index]>=0: result=max(result, lst[index])  # We'll make sure it is set later. 
        helper(lst, index+1)
    helper(lst, 0)
    if (result>-1): return result
    else: return -1
# Driver Code
if __name__ == '__main__':
    lst = [4, 1, 2, 2, 3, 1]
    print("Result of " + \
          "'search(lst)':", search(lst))