"""
Write a function to find the specified number of largest products from two given lists, selecting one factor from each list.
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]
"""

def large_product(list1, list2, n):
    """ Function that takes two lists and finds the required number of largest products from two given lists, selecting one factor from each list.
        :param list1: first list to be operated on
        :param list2: second list to be operated on
        :param n: product count from a combination of elements
    """
    # Create an empty list to store the largest products created. 
    result = []
    for i in range(n): 
        # Get the index of the first and last element from each list, then pick one factor to operate on.
        start = min([i[0] for i in enumerate(list1)])
        end = max([i[1] for i in enumerate(list2)]) + 1
    # Make a product of the chosen elements.
        result.append(list(factor) * factor_count) for factor, factor_count in zip(i[0],i[1:])
    return list(result) # Get all elements from the returned largest products list as one. 
```