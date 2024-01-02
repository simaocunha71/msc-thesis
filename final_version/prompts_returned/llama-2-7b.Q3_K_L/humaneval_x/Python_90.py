
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    def _next_smallest(lst):
        if not lst or len(lst) == 0:
            return None
        
        result = lst[0]

        for item in range(len(lst), -1, -1):
            if lst[item-1] < result:
                result = lst[item-1]
        
        return result
    return _next_smallest
