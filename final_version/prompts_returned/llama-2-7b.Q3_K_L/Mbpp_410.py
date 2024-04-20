"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""

def find_min(lst):
    """
    :type lst: List[object]
    :rtype: int
    """
    if not type(lst) == list and len(lst) != 0:
        return min(lst)
    
    else:
        minimum = float('inf')
        
        for val in lst:
            if type(val)==str or type(val) == int:
                if val < minimum:
                    minimum = val
                    return minimum
            
            elif type(val) == float:
                if val < minimum:
                    minimum = val
                    return minimum
            
        return minimum

if __name__ == "__main__":
    # Example 1: ['a', 'b', 'c', 'd']
    print(find_min(['a', 'b', 'c', 'd']))
    
    # Example 2: [3, 2, -5]
    print(find_min([3, 2, -5]))